import globals
import os

import ansi_codes as ac


def is_first_run() -> bool:
    if not globals.FMDATA.exists():
        os.mkdir(globals.FMDATA)
                
        return True
    return False
        

def debug(text: str) -> None:
    print(f"{ac.green}{text}{ac.clear}")


def info(*text: str) -> None:
    for line in text:
        print(line)


def broken_config_error() -> None:
    print(
        "ftagger: There's an issue with ftagger's dotfiles. Did you " \
        "edit them? If not, please open an issue on the GitHub repo, " \
        "https://github.com/CharlieODwyer/ftagger.git. You should now " \
        "run the 'rd' command."
    )