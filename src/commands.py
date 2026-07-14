import os
import json
import globals

from pathlib import Path

from utils import *


def help() -> None:
    info(
        "|   Name   |                   Description                    |           Usage               |",
        "|----------|--------------------------------------------------|-------------------------------|",
        "|    at    |    adds a tag to file or folder                  |    at <path> <tag>            |",
        "|    rt    |    removes a tag from file or folder             |    rt <path> <tag>            |",
        "|    gi    |    gets items by tag                             |    gi <path> <tag>            |",
        "|    gt    |    gets tags of a file or folder                 |    gt <path>                  |",
        "|    li    |    lists files and folders and their tags        |    li <path>                  |",
        "|    rc    |    tags all items in a directory                 |    rc <path> <tag> <depth>    |",
        "|    rr    |    removes a tag from all items in a directory   |    rr <path> <tag> <depth>    |",
        "|    ca    |    creates an alias for a command                |    ca <command> <alias>       |",
        "|    ra    |    removes an alias                              |    ra <alias>                 |",
        "|    la    |    lists all existing aliases                    |    la                         |",
        "|    rd    |    resets all alias data                         |    rd                         |",
    )


def add_tag(path: str, tag: str) -> None:
    tag: bytes = tag.encode('utf-8')


    try:
        current_tag: bytes = os.getxattr(path=path, attribute=b"user.tags")
    except:
        current_tag = "".encode('utf-8')


    if current_tag != b'': 
        combined_tag: bytes = current_tag + ",".encode('utf-8') + tag
    else:
        combined_tag: bytes = tag


    try:
        os.setxattr(path=path, attribute=b"user.tags", value=combined_tag)
        
    except PermissionError:
        print("Permission denied")


def remove_tag(path: str, tag: str) -> None:
    values: list[str] = os.getxattr(path=path, attribute=b"user.tags").decode('utf-8').split(",")
    values.remove(tag)
    values = ",".join(values).encode('utf-8')


    try:
        os.setxattr(path=path, attribute=b"user.tags", value=values)

    except PermissionError:
        print("Permission denied")


def get_items_by_tag(path: str, value: str) -> None:
    for item in Path(path).rglob("*"):
        try:
            tags = os.getxattr(path=item, attribute=b"user.tags").decode('utf-8').split(",")
        
        except:
            tags = []


        if value in tags:
            if os.path.isdir(item):
                print(f"{ac.blue}{item}{ac.clear}")

            else:
                print(item)


def get_tags(path: str) -> None:
    try:
        tags = os.getxattr(path=path, attribute=b"user.tags").decode('utf-8')

        tags = tags.split(",")

    except:
        tags = ["~"]

    for i in tags:
        if tags == []:
            print("~")
        else:
            print(i)


def list_items_and_tags(path: str) -> None:
    for item in Path(path).rglob("*"):
        try:
            tags = os.getxattr(path=item, attribute=b"user.tags").decode('utf-8')
        except:
            tags = ""

        if os.path.isdir(item):
            print(f"{ac.blue}{ac.bold}{str(item): <30}{ac.clear}{tags: >15}")
        else:   
            print(f"{str(item): <30}{tags: >15}")


def recursive_add_tag(path: str, tag: str, depth: int) -> None:
    depth = int(depth)

    for item in Path(path).rglob("*"):
        if len(str(item).split("/")) <= depth:
            add_tag(item, tag=tag)


def recursive_remove_tag(path: str, tag: str, depth: int) -> None:
    depth = int(depth)

    for item in Path(path).rglob("*"):
        if len(str(item).split("/")) <= depth:
            try:
                remove_tag(item, tag)
            except:
                print(f"Item {item} doesn't have tag {tag}")


def create_alias(command: str, alias: str) -> None:
    with open(globals.FMDEFAULT, "r") as file:
        try:
            commands_dict: dict = json.load(file)
        except:
            commands_dict: dict = {}


        with open(globals.FMALIASLOOKUP, "r") as fm_alias_lookup_file, open(globals.FMALIASES, "r") as fm_alias_file:
            try:
                lookup_dict: dict = json.load(fm_alias_lookup_file)
            except:
                lookup_dict: dict = {}


            try:
                alias_dict: dict = json.load(fm_alias_file)
            except:
                alias_dict: dict = {}


            lookup_dict.update({ alias: command })
            alias_dict.update({ alias: commands_dict[command] })


        with open(globals.FMALIASLOOKUP, "w") as fm_alias_lookup_file, open(globals.FMALIASES, "w") as fm_alias_file:
            json.dump(lookup_dict, fm_alias_lookup_file, indent=4)
            json.dump(alias_dict, fm_alias_file, indent=4)


    with open(globals.FMUNDOLOOKUP, "r") as file:
        undo_dict = json.load(file)

        undo_dict.update({ alias: undo_dict[command] })


    with open(globals.FMUNDOLOOKUP, "w") as file:
        json.dump(undo_dict, file, indent=4)


def remove_alias(alias: str) -> None:
    with open(globals.FMALIASLOOKUP, "r") as fm_alias_lookup_file, open(globals.FMALIASES, "r") as fm_aliases_file:
        try:
            alias_dict: dict = json.load(fm_aliases_file)
            lookup_dict: dict = json.load(fm_alias_lookup_file)
        except:
            alias_dict: dict = {}
            lookup_dict: dict = {}
            error("Please use the 'rd' command and re-add your aliases")


        try:
            lookup_dict.pop(alias)
            alias_dict.pop(alias)
        except:
            error("Alias does not exist")
            return


    with open(globals.FMALIASLOOKUP, "w") as fm_alias_lookup_file, open(globals.FMALIASES, "w") as fm_aliases_file:
        try:
            json.dump(lookup_dict, fm_alias_lookup_file, indent=4)
            json.dump(alias_dict, fm_aliases_file, indent=4)
        except:
            json.dump({}, fm_alias_lookup_file, indent=4)
            json.dump({}, fm_aliases_file, indent=4)


    with open(globals.FMUNDOLOOKUP, "r") as file:
        undo_dict = json.load(file)

        undo_dict.pop(alias)


    with open(globals.FMUNDOLOOKUP, "w") as file:
        json.dump(undo_dict, file, indent=4)
        

def list_aliases() -> None:
    with open(globals.FMALIASLOOKUP, "r") as file:
        aliases: dict = json.load(file)

        for key, value in aliases.items():
            print(f"{key}: {value}")


def reset_data() -> None:
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


    with open(globals.FMUNDOLOOKUP) as file:
        default_data: dict = {
            "at": "rt",
            "rt": "at",
            "rc": "rr",
            "rr": "rc",
            "ca": "ra",
            "ra": "ca",
            "tag": "rt"
        }


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

