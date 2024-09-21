import functools
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from repo.toolkit import core


class Inputs(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="INPUT_")

    algo: str = "sha256"
    clobber: bool = False
    pre_release: bool = False
    repo: str
    tag: str

    @functools.cached_property
    def changelog(self) -> str | None:
        fpath: Path = Path(core.get_input("CHANGELOG_FILE"))
        text: str = fpath.read_text().strip()
        body: str
        _, _, body = text.partition("\n")
        if not body:
            return None
        return body.strip()

    @functools.cached_property
    def files(self) -> list[Path]:
        files: list[Path] = []
        cwd: Path = Path.cwd()
        for line in core.get_multiline_input("FILES"):
            files.extend(cwd.glob(line))
        return files
