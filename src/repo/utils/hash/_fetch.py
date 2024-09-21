from repo import utils
from repo.toolkit.github import GitHub
from repo.utils import hash


async def fetch_hashsums(gh: GitHub, tag: str, algo: str = "sha256") -> dict[str, str]:
    fname: str = hash.hashfile_name(algo)
    try:
        text: str = await gh.release_download(tag, fname)
    except FileNotFoundError:
        return {}
    hashsums: dict[str, str] = {}
    for line in utils.splitlines(text):
        hsum: str
        hsum, fname = line.split(maxsplit=1)
        hashsums[fname] = hsum
    return hashsums
