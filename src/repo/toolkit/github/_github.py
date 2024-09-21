import asyncio
from collections.abc import Coroutine, Sequence
from pathlib import Path

import githubkit
import githubkit.exception
from githubkit.utils import UNSET
from githubkit.versions.latest.models import Release, ReleaseAsset
from githubkit.versions.rest import RestVersionSwitcher

import repo.utils.hash as h
from repo.typing import StrPath


class GitHub:
    owner: str
    repo: str
    _gh: githubkit.GitHub

    def __init__(self, repo: str) -> None:
        self._gh = githubkit.GitHub(githubkit.ActionAuthStrategy())
        self.owner, _, self.repo = repo.partition("/")

    @property
    def rest(self) -> RestVersionSwitcher:
        return self._gh.rest

    async def get_release_by_tag(self, tag: str) -> Release:
        resp: githubkit.Response[
            Release
        ] = await self.rest.repos.async_get_release_by_tag(self.owner, self.repo, tag)
        return resp.parsed_data

    async def release_exists(self, tag: str) -> Release | None:
        try:
            release: Release = await self.get_release_by_tag(tag)
        except githubkit.exception.RequestFailed as err:
            if err.response.status_code == 404:
                return None
            raise
        return release

    async def release_create(
        self,
        tag: str,
        *,
        assets: Sequence[StrPath] | None = None,
        changelog: str | None = None,
        hash_algo: str = "sha256",
        pre_release: bool = False,
    ) -> Release:
        resp: githubkit.Response[Release] = await self.rest.repos.async_create_release(
            self.owner,
            self.repo,
            tag_name=tag,
            name=tag,
            body=changelog or UNSET,
            prerelease=pre_release,
            generate_release_notes=not changelog,
        )
        release: Release = resp.parsed_data
        await self.release_upload(release.id, assets, hash_algo)
        return release

    async def release_delete(self, release: Release) -> None:
        await self.rest.repos.async_delete_release(self.owner, self.repo, release.id)
        await self.rest.git.async_delete_ref(
            self.owner, self.repo, f"tags/{release.tag_name}"
        )

    async def release_download(self, tag: str, filename: str) -> str:
        release: Release = await self.get_release_by_tag(tag)
        asset: ReleaseAsset | None = next(
            (asset for asset in release.assets if asset.name == filename), None
        )
        if asset is None:
            msg: str = f"Asset {filename!r} not found in release {tag!r}"
            raise FileNotFoundError(msg)
        resp: githubkit.Response = await self._gh.arequest(
            "GET", asset.browser_download_url
        )
        return resp.text

    async def release_upload(
        self,
        release_id: int,
        assets: Sequence[StrPath] | None = None,
        hash_algo: str = "sha256",
    ) -> None:
        if not assets:
            return
        hashsums: dict[str, str] = h.hashfiles(assets, hash_algo)
        jobs: list[Coroutine] = []
        for asset in assets:
            fpath: Path = Path(asset)
            jobs.append(
                self.rest.repos.async_upload_release_asset(
                    self.owner,
                    self.repo,
                    release_id,
                    fpath.name,
                    data=fpath.read_bytes(),
                )
            )
            jobs.append(
                self.rest.repos.async_upload_release_asset(
                    self.owner,
                    self.repo,
                    release_id,
                    h.with_ext(fpath.name, hash_algo),
                    data=h.dump({fpath.name: hashsums[fpath.name]}).encode(),
                )
            )
        jobs.append(
            self.rest.repos.async_upload_release_asset(
                self.owner,
                self.repo,
                release_id,
                h.hashfile_name(hash_algo),
                data=h.dump(hashsums).encode(),
            )
        )
        await asyncio.gather(*jobs)
