import dataclasses
import pathlib
from typing import Self

from repo.toolkit import core


@dataclasses.dataclass(kw_only=True)
class Input:
    repo: str
    tag: str
    files: list[pathlib.Path]
    changelog: str | None
    checksum: str
    pre_release: bool

    recreate: bool

    @classmethod
    def get(cls) -> Self:
        repo: str = core.input_str("repo")
        tag: str = core.input_str("tag")

        return cls(
            changelog=_changelog(),
            checksum=core.input_str("checksum"),
            files=_files(),
            pre_release=core.input_bool("pre-release"),
            recreate=core.input_bool("recreate"),
            repo=repo,
            tag=tag,
        )


def _changelog() -> str | None:
    changelog_file = pathlib.Path(core.input_str("changelog-file"))
    changelog: str = changelog_file.read_text().strip()
    parts: list[str] = changelog.split("\n", maxsplit=1)
    if len(parts) <= 1:
        return None
    return parts[1].strip()


def _files() -> list[pathlib.Path]:
    patterns: list[str] = core.input_multiline("files")
    files: list[pathlib.Path] = []
    for p in patterns:
        files.extend(pathlib.Path.cwd().glob(p))
    return files
