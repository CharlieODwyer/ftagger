import commands
import json
import globals

from sys import argv, modules
from utils import *


def call(args: list[str]) -> None:
    with open(globals.FMDEFAULT, "r") as file:
        commands_dict: dict = json.load(file)

    with open(globals.FMALIASES, "r") as f:
        alias_dict: dict = json.load(f)

        try:
            commands_dict.update(alias_dict)
        except:
            pass


    for key, value in commands_dict.items():
        try:
            commands_dict[key] = getattr(commands, value)
        except:
            try:
                commands_dict[key] = getattr(modules[__name__], value)
            except:
                debug(commands_dict)
                error(f"There may be an invalid alias. Please check the aliases you've added: {key}: {value}")


    try:
        match len(args):
            case 2:
                commands_dict[args[1]]()

            case 3:
                commands_dict[args[1]](args[2])
                
            case 4:
                commands_dict[args[1]](args[2], args[3])

            case 5:
                commands_dict[args[1]](args[2], args[3], args[4])

    except Exception:
        debug("Error handling is not yet fully implemented, as I have decided to change how to impement it. For debugging purposes, the exception will now be raised.")
        raise Exception
        


def undo() -> None:
    with open(globals.FMPREVIOUSCOMMAND, "r") as file:
        previous_commands: list[str] = json.load(file)


        with open(globals.FMUNDOLOOKUP, "r") as f:
            undo_dict: dict = json.load(f)

            
            for command in list(previous_commands.values())[::-1]:
                debug(command)
                try:
                    command[1] = undo_dict[command[1]]
                    call(command)
                except:
                    pass


def main() -> None:
    check_for_first_run()
    
    command: list[str] = argv


    with open(globals.FMPREVIOUSCOMMAND, "r") as file:
        previous_commands: dict = json.load(file)
        
        previous_commands.update({
            "0": previous_commands["1"],
            "1": previous_commands["2"],
            "2": previous_commands["3"],
            "3": previous_commands["4"],
            "4": command,
        })
        

    with open(globals.FMPREVIOUSCOMMAND, "w") as file:
        json.dump(previous_commands, file, indent=4)


    call(command)

            
if __name__ == "__main__":
    main()
