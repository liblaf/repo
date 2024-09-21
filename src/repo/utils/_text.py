from collections.abc import Generator


def splitlines(s: str) -> Generator[str, None, None]:
    for line in s.strip().splitlines():
        stripped_line: str = line.strip()
        if stripped_line:
            yield stripped_line
