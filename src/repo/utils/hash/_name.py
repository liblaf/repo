_ALGO_TO_FILENAME: dict[str, str] = {"blake2b": "b2sums.txt"}


def hashsum_filename(algo: str) -> str:
    """Return the hashsum filename for a given algorithm."""
    if algo in _ALGO_TO_FILENAME:
        return _ALGO_TO_FILENAME[algo]
    return algo + "sums.txt"


def single_hashsum_filename(fname: str, algo: str) -> str:
    """Return the hashsum filename for a given file and algorithm."""
    return fname + "." + algo
