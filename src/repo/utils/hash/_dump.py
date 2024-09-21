def dump(hashsums: dict[str, str]) -> str:
    text: str = ""
    for fname, hsum in hashsums.items():
        text += hsum + "  " + fname + "\n"
    return text
