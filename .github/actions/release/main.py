import dataclasses
import functools
import glob
import hashlib
import json
import operator
import os
import pathlib
import subprocess
import tempfile
import time
from typing import Self, TypedDict


def input_bool(name: str) -> bool:
    val: str | None = os.getenv(name)
    if val in ["true", "True", "TRUE"]:
        return True
    if val in ["false", "False", "FALSE"]:
        return False
    raise TypeError(f"""\
Input does not meet YAML 1.2 "Core Schema" specification: {name}
Support boolean input list: `true | True | TRUE | false | False | FALSE`\
""")


def input_files() -> list[pathlib.Path]:
    patterns: list[str] = os.getenv("INPUT_FILES", "").splitlines()
    patterns = [pattern.strip() for pattern in patterns]
    patterns = [pattern for pattern in patterns if pattern]
    files: list[str] = functools.reduce(
        operator.iconcat, [glob.glob(pattern) for pattern in patterns], []
    )
    return [pathlib.Path(file) for file in files]


def input_changelog() -> str | None:
    release_please_pr: str | None = os.getenv("INPUT_RELEASE_PLEASE_PR")
    if not release_please_pr:
        return None

    class Pr(TypedDict):
        body: str

    pr: Pr = json.loads(release_please_pr)
    body: str = pr["body"]
    body = body.split("---", maxsplit=1)[1]
    body = body.rsplit("---", maxsplit=1)[0]
    return body.strip()


@dataclasses.dataclass(kw_only=True)
class Input:
    changelog: str | None = None
    checksum: str
    files: list[pathlib.Path]
    pre_release: bool
    recreate: bool
    repo: str
    tag: str

    @classmethod
    def from_env(cls) -> Self:
        return cls(
            changelog=input_changelog(),
            checksum=os.getenv("INPUT_CHECKSUM", "blake2b"),
            files=input_files(),
            pre_release=input_bool("INPUT_PRE_RELEASE"),
            recreate=input_bool("INPUT_RECREATE"),
            repo=os.environ["INPUT_REPO"],
            tag=os.environ["INPUT_TAG"],
        )


ALGORITHM_NAMES: dict[str, str] = {"blake2b": "b2"}


def checksum(algo: str, file: pathlib.Path) -> str:
    hasher = hashlib.new(algo)
    hasher.update(file.read_bytes())
    return hasher.hexdigest()


def algorithm_name(algo: str) -> str:
    return ALGORITHM_NAMES.get(algo, algo)


def prepare_assets(
    cksum_algo: str, files: list[pathlib.Path], tmpdir: pathlib.Path
) -> dict[str, str]:
    checksums: dict[str, str] = {f.name: checksum(cksum_algo, f) for f in files}
    if checksums:
        algo_name: str = algorithm_name(cksum_algo)
        with (tmpdir / f"{algo_name}sums.txt").open("w") as fp:
            for name in sorted(checksums):
                fp.write(f"{checksums[name]}  {name}\n")
    return checksums


def release_exists(repo: str, tag: str) -> bool:
    proc: subprocess.CompletedProcess[bytes] = subprocess.run(
        ["gh", "release", f"--repo={repo}", "view", tag]
    )
    return proc.returncode == 0


def fetch_checksums(repo: str, tag: str) -> dict[str, str]:
    proc: subprocess.CompletedProcess[str] = subprocess.run(
        [
            "gh",
            "release",
            f"--repo={repo}",
            "download",
            tag,
            "--output=-",
            "--pattern=*sums.txt",
        ],
        stdout=subprocess.PIPE,
        text=True,
    )
    if proc.returncode != 0:
        return {}
    checksums: dict[str, str] = {}
    for line in proc.stdout.splitlines():
        line: str = line.strip()
        if not line:
            continue
        digest: str
        name: str
        digest, name = line.split(maxsplit=1)
        checksums[name] = digest
    return checksums


def gh_release_create(
    repo: str,
    tag: str,
    files: list[pathlib.Path] | None = None,
    changelog: str | None = None,
    pre_release: bool = False,
) -> None:
    args: list[str] = ["gh", "release", f"--repo={repo}", "create", tag]
    if files:
        args.extend(str(f) for f in files)
    if changelog:
        args.append(f"--notes={changelog}")
    else:
        args.append("--generate-notes")
    if pre_release:
        args.append("--prerelease")
    args.append(f"--title={tag}")
    subprocess.run(args, check=True)


def gh_release_delete(repo: str, tag: str) -> None:
    subprocess.run(
        [
            "gh",
            "release",
            f"--repo={repo}",
            "delete",
            tag,
            "--cleanup-tag",
        ],
        check=True,
    )
    # TODO: fix <https://github.com/cli/cli/issues/8458#issuecomment-1854326401> in a more elegant way
    time.sleep(3)


def main() -> None:
    input: Input = Input.from_env()
    with tempfile.TemporaryDirectory() as tmpdir_:
        tmpdir = pathlib.Path(tmpdir_)
        checksums: dict[str, str] = prepare_assets(input.checksum, input.files, tmpdir)
        if release_exists(input.repo, input.tag):
            checksums_remote: dict[str, str] = fetch_checksums(input.repo, input.tag)
            if checksums == checksums_remote:
                print("::notice::Checksums match, skipping release")
                return
            if input.recreate:
                gh_release_delete(input.repo, input.tag)
            subprocess.run(
                [
                    "gh",
                    "release",
                    f"--repo={input.repo}",
                    "upload",
                    input.tag,
                    *list(map(str, input.files)),
                ],
                check=True,
            )


if __name__ == "__main__":
    main()
