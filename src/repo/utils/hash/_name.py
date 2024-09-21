_ALGO_TO_FILENAME: dict[str, str] = {"blake2b": "b2sums.txt"}


def hashfile_name(algo: str) -> str:
    if algo in _ALGO_TO_FILENAME:
        return _ALGO_TO_FILENAME[algo]
    return algo + "sums.txt"


def with_ext(fname: str, algo: str) -> str:
    return fname + "." + algo
