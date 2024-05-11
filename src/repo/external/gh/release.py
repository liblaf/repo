import pathlib
import subprocess


class GhRelease:
    repo: str | None = None

    def __init__(self, repo: str | None = None) -> None:
        self.repo = repo

    @property
    def args(self) -> list[str]:
        args: list[str] = ["gh", "release"]
        if self.repo:
            args.append("--repo=" + self.repo)
        return args

    def create(
        self,
        tag: str,
        files: list[pathlib.Path] | None = None,
        *,
        changelog: str | None = None,
        pre_release: bool = False,
    ) -> None:
        args: list[str] = [*self.args, "create", tag]
        if files:
            args.extend(str(f) for f in files)
        if changelog:
            args.append("--notes=" + changelog)
        else:
            args.append("--generate-notes")
        if pre_release:
            args.append("--prerelease")
        args.append("--title=" + tag)
        subprocess.run(args, check=True)

    def delete(self, tag: str, *, cleanup_tag: bool = True) -> None:
        args: list[str] = [*self.args, "delete", tag]
        if cleanup_tag:
            args.append("--cleanup-tag")
        subprocess.run(args, check=True)

    def download(self, tag: str, pattern: str) -> str:
        proc: subprocess.CompletedProcess[str] = subprocess.run(
            [*self.args, "download", tag, "--output=-", "--pattern=" + pattern],
            check=True,
            text=True,
        )
        return proc.stdout

    def upload(
        self, tag: str, files: list[pathlib.Path], *, clobber: bool = True
    ) -> None:
        args: list[str] = [*self.args, "upload", tag]
        args.extend(str(f) for f in files)
        if clobber:
            args.append("--clobber")
        subprocess.run(args, check=True)

    def view(self, tag: str) -> bool:
        proc: subprocess.CompletedProcess[bytes] = subprocess.run(
            [*self.args, "view", tag],
            check=False,
        )
        return proc.returncode == 0
