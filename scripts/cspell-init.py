import json
import subprocess
import sys
import tempfile

ignore_paths: list[str] = sorted(
    ["**/.cspell.json", "**/*-lock.*", "**/*.lock", *sys.argv[1:]]
)
with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as fp:
    json.dump(
        {
            "ignorePaths": ignore_paths,
            "allowCompoundWords": True,
        },
        fp,
    )
    fp.flush()
    process: subprocess.CompletedProcess[str] = subprocess.run(
        [
            "cspell",
            "lint",
            "--config",
            fp.name,
            "--words-only",
            "--unique",
            "--exclude",
            ".git",
            "--no-exit-code",
            "--dot",
            "--gitignore",
            "--color",
            ".",
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=sys.stderr,
        check=True,
        text=True,
    )
    stdout: str = process.stdout
words: set[str] = set(word.lower() for word in stdout.splitlines())
json.dump(
    {
        "words": sorted(words),
        "ignorePaths": ignore_paths,
        "allowCompoundWords": True,
    },
    sys.stdout,
    ensure_ascii=False,
    sort_keys=False,
)
