import os


def input_str(name: str, default: str = "") -> str:
    env_name: str = "INPUT_" + name.upper().replace("-", "_")
    return os.getenv(env_name, default)


def input_bool(name: str) -> bool:
    val: str | None = input_str(name)
    if val in ["true", "True", "TRUE"]:
        return True
    if val in ["false", "False", "FALSE"]:
        return False
    msg: str = f"""\
Input does not meet YAML 1.2 "Core Schema" specification: {name}
Support boolean input list: `true | True | TRUE | false | False | FALSE`\
"""
    raise TypeError(msg)


def input_multiline(name: str) -> list[str]:
    val: str = input_str(name)
    lines: list[str] = val.splitlines()
    lines = [line.strip() for line in lines]
    return [line for line in lines if line]


def notice(msg: str) -> None:
    print("::notice::" + msg)
