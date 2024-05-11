import hashlib
import pathlib
import subprocess

from repo.external.gh import Gh

ALGORITHM_NAMES: dict[str, str] = {"blake2b": "b2"}


def algorithm_name(algo: str) -> str:
    return ALGORITHM_NAMES.get(algo, algo)


def checksum(algo: str, file: pathlib.Path) -> str:
    hasher = hashlib.new(algo)
    hasher.update(file.read_bytes())
    return hasher.hexdigest()


def prepare(
    cksum_algo: str, files: list[pathlib.Path], tmpdir: pathlib.Path
) -> tuple[dict[str, str], pathlib.Path | None]:
    cksums: dict[str, str] = {f.name: checksum(cksum_algo, f) for f in files}
    if cksums:
        algo_name: str = algorithm_name(cksum_algo)
        cksums_path: pathlib.Path = tmpdir / (algo_name + "sums.txt")
        with cksums_path.open("w") as fp:
            for name in sorted(cksums):
                fp.write(f"{cksums[name]}  {name}\n")
        return cksums, cksums_path
    return {}, None


def fetch_checksums(repo: str, tag: str) -> dict[str, str]:
    try:
        cksums_str: str = Gh().release(repo).download(tag, "*sums.txt")
        cksums: dict[str, str] = {}
        for line_ in cksums_str.splitlines():
            line: str = line_.strip()
            if not line:
                continue
            digest: str
            name: str
            digest, name = line.split(maxsplit=1)
            cksums[name] = digest
    except subprocess.CalledProcessError:
        return {}
    else:
        return cksums
