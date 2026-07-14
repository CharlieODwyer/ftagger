import json
import globals
import os

import ansi_codes as ac


def check_for_first_run() -> bool:
    if not globals.FMDATA.exists():
        os.mkdir(globals.FMDATA)
                
        with open(globals.FMALIASLOOKUP, "w") as file:
            json.dump({}, file, indent=4)


        with open(globals.FMALIASES, "w") as file:
            json.dump({}, file, indent=4)


        with open(globals.FMDEFAULT, "w") as file:
            default_data: dict = {
                "--help": "help",
                "at": "add_tag",
                "rt": "remove_tag",
                "gi": "get_items_by_tag",
                "gt": "get_tags",
                "li": "list_items_and_tags",
                "rc": "recursive_add_tag",
                "rr": "recursive_remove_tag",
                "ca": "create_alias",
                "ra": "remove_alias",
                "la": "list_aliases",
                "rd": "reset_data",
                "un": "undo"
            }

            json.dump(default_data, file, indent=4)


        with open(globals.FMUNDOLOOKUP, "w") as file:
            default_data: dict = {
                "at": "rt",
                "rt": "at",
                "rc": "rr",
                "rr": "rc",
                "ca": "ra",
                "ra": "ca",
                "tag": "rt"
            }

            json.dump(default_data, file, indent=4)


        with open(globals.FMPREVIOUSCOMMAND, "w") as file:
            default_data: dict = {
                "0": [
                    "Default",
                ],
                "1": [
                    "Default",
                ],
                "2": [
                    "Default",
                ],
                "3": [
                    "Default",
                ],
                "4": [
                    "Default",
                ]
            }

            json.dump(default_data, file, indent=4)
        

def error(text: str) -> None:
    print(f"{ac.red}{text}{ac.clear}")


def debug(text: str) -> None:
    print(f"{ac.green}{text}{ac.clear}")


def info(*text: str) -> None:
    for line in text:
        print(line)