import hashlib
from collections.abc import Iterable
from pathlib import Path

from repo.typing import StrPath


def hashsum(fpath: StrPath, algo: str = "sha256") -> str:
    fpath: Path = Path(fpath)
    hasher: hashlib._Hash = hashlib.new(algo)
    hasher.update(fpath.read_bytes())
    return hasher.hexdigest()


def hashfiles(fpaths: Iterable[StrPath], algo: str = "sha256") -> dict[str, str]:
    hashsums: dict[str, str] = {}
    for _fpath in fpaths:
        fpath: Path = Path(_fpath)
        hashsums[fpath.name] = hashsum(fpath, algo)
    return hashsums
