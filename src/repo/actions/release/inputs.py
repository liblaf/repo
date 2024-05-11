import dataclasses
import json
import pathlib
from typing import Self, TypedDict

from repo.toolkit import core


@dataclasses.dataclass(kw_only=True)
class Input:
    changelog: str | None
    checksum: str
    files: list[pathlib.Path]
    pre_release: bool
    repo: str
    tag: str

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
    pr_str: str = core.input_str("release-please-pr")
    if not pr_str:
        return None

    class Pr(TypedDict):
        body: str

    pr: Pr = json.loads(pr_str)
    body: str = pr["body"]
    body = body.split("---", maxsplit=1)[1]
    body = body.rsplit("---", maxsplit=1)[0]
    return body.strip()


def _files() -> list[pathlib.Path]:
    patterns: list[str] = core.input_multiline("files")
    files: list[pathlib.Path] = []
    for p in patterns:
        files.extend(pathlib.Path.cwd().glob(p))
    return files
