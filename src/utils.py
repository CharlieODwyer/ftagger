import ansi_codes as ac

def error(text: str) -> None:
    print(f"{ac.red}{text}{ac.clear}")


def debug(text: str) -> None:
    print(f"{ac.green}{text}{ac.clear}")


def info(*text: str) -> None:
    for line in text:
        print(line)