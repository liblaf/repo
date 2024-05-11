import pathlib
import tempfile

from repo.actions.release import asset
from repo.actions.release.inputs import Input
from repo.external.gh import Gh, GhRelease
from repo.toolkit import core


def main() -> None:
    inputs: Input = Input.get()
    with tempfile.TemporaryDirectory() as tmpdir_:
        tmpdir = pathlib.Path(tmpdir_)
        cksums: dict[str, str]
        cksums_path: pathlib.Path | None
        cksums, cksums_path = asset.prepare(inputs.checksum, inputs.files, tmpdir)
        if cksums_path:
            inputs.files.append(cksums_path)
        release_api: GhRelease = Gh().release(inputs.repo)
        release_exists: bool = release_api.view(inputs.tag)
        if release_exists:
            cksums_remote: dict[str, str] = asset.fetch_checksums(
                inputs.repo, inputs.tag
            )
            if cksums == cksums_remote:
                core.notice(f"Checksums match, skipping release: {inputs.tag}")
                return
            if inputs.recreate:
                release_api.delete(inputs.tag)
                release_api.create(
                    inputs.tag,
                    inputs.files,
                    changelog=inputs.changelog,
                    pre_release=inputs.pre_release,
                )
                core.notice(f"Recreated release: {inputs.tag}")
            else:
                release_api.upload(inputs.tag, inputs.files)
        else:
            release_api.create(
                inputs.tag,
                inputs.files,
                changelog=inputs.changelog,
                pre_release=inputs.pre_release,
            )
            core.notice(f"Created release: {inputs.tag}")


if __name__ == "__main__":
    main()
