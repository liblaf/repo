import repo.utils.hash as h
from repo import utils
from repo.toolkit import core
from repo.toolkit.github import GitHub

from ._inputs import Inputs


@utils.action()
async def main(inputs: Inputs) -> None:
    gh: GitHub = GitHub(inputs.repo)
    create: bool = False
    if (release := await gh.release_exists(inputs.tag)) is not None:
        hashsums_local: dict[str, str] = h.hashfiles(inputs.files, inputs.algo)
        hashsums_remote: dict[str, str] = await h.fetch_hashsums(
            gh, inputs.tag, inputs.algo
        )
        if hashsums_local == hashsums_remote:
            core.notice(f"Hashsums match, skip release: {inputs.tag!r}")
            return
        if inputs.clobber:
            await gh.release_delete(release)
            create = True
            core.notice(f"Recreate release: {inputs.tag!r}")
        else:
            core.notice(f"Update release: {inputs.tag!r}")
            await gh.release_upload(release.id, inputs.files, inputs.algo)
    else:
        create = True
        core.notice(f"Create release: {inputs.tag!r}")
    if create:
        await gh.release_create(
            inputs.tag,
            assets=inputs.files,
            changelog=inputs.changelog,
            hash_algo=inputs.algo,
            pre_release=inputs.pre_release,
        )
