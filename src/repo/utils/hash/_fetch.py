from loguru import logger

from repo import utils
from repo.toolkit.github import GitHub
from repo.utils import hash


async def fetch_hashsums(gh: GitHub, tag: str, algo: str = "sha256") -> dict[str, str]:
    fname: str = hash.hashsum_filename(algo)
    try:
        text: str = await gh.release_download(tag, fname)
    except FileNotFoundError:
        logger.warning(f"Hashsum file {fname!r} not found in release {tag!r}")
        return {}
    hashsums: dict[str, str] = {}
    for line in utils.splitlines(text):
        hsum: str
        hsum, fname = line.split(maxsplit=1)
        hashsums[fname] = hsum
    return hashsums
