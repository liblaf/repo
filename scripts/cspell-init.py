import json
import subprocess
import sys
import tempfile

with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as fp:
    json.dump(
        {
            "ignorePaths": [".cspell.json", "*-lock.*", "*.lock"],
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
            sys.argv[1] if len(sys.argv) > 1 else ".",
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=sys.stderr,
        check=True,
        text=True,
    )
    stdout: str = process.stdout
words: set[str] = set(word.lower() for word in stdout.splitlines())
config: str = json.dumps(
    {
        "words": sorted(words),
        "ignorePaths": [".cspell.json", "*-lock.*", "*.lock"],
        "allowCompoundWords": True,
    },
    ensure_ascii=False,
    sort_keys=False,
)
json.dump(
    {
        "words": sorted(words),
        "ignorePaths": [".cspell.json", "*-lock.*", "*.lock"],
        "allowCompoundWords": True,
    },
    sys.stdout,
    ensure_ascii=False,
    sort_keys=False,
)
