# Preface

Most of this project was created before I began using GitHub, which is why the first commit is already almost finished.

Most error handling should be done now. I am now working on ironing out a few bugs.

This is just a personal project that I will use for college. The goal is not for it to be perfect, but for it to work. 

Any criticism is welcome — especially about my code. It is also worth noting that this is the first documentation I've written, so I apologise if it's not up to your expected standard. Please also tell me how I can improve the docs. Thank you. 

This programme has only been tested on Linux. Due to its use of the 'os' module and extended attributes, it may not work on all operating systems.


# What Is This Project?

This project is a very simple command-line file tagger. Its main function is to tag files and folders to make organisiation easier. I wrote this programme, as I am going to start college soon, and I wanted a simple way to organise my notes. It is just a personal project. Below is an outline of the features:

- Tagging files and folders. The 'os' module is used to tag items using extended attributes. Command: at

- Removing tags from files and folders. Command: rt

- Searching for items in a directory with a given tag. Command: gi

- Getting the tags of an item. Command: gt

- Listing all items in a given directory, along with their tags. Command: li

- Creating and removing aliases for commands. Commands: ca, ra

- Listing all aliases. Command: la

- Recursively adding tags to or removing tags from items to a certain depth. Commands: rc, rr

- Resetting all dotfiles in ~/.fmdata (aliases, lookup tables, etc). Command: rd

- Undo. Undo the previous undoable command, up to five commands ago.


# Help

Here is the output of running the command with the --help flag:

```
|   Name   |                   Description                    |           Usage               |
|---------------------------------------------------------------------------------------------|
|    at    |    adds a tag to a file or folder                |    at <path> <tag>            |
|    rt    |    removes a tag from file or folder             |    rt <path> <tag>            |
|    gi    |    searches items by tag                         |    gi <path> <tag>            |
|    gt    |    displays tags of a file or folder             |    gt <path>                  |
|    li    |    lists files and folders and their tags        |    li <path>                  |
|    rc    |    tags all items in a directory                 |    rc <path> <tag> <depth>    |
|    rr    |    removes a tag from all items in a directory   |    rr <path> <tag> <depth>    |
|    ca    |    creates an alias for a command                |    ca <command> <alias>       |
|    ra    |    removes an alias                              |    ra <alias>                 |
|    la    |    lists all existing aliases                    |    la                         |
|    rd    |    resets all alias data                         |    rd                         |
```


# Installation and Uninstallation
### To install
```
pip install ftagger

OR

pipx install ftagger
```

### To uninstall (one extra step)
```
pip uninstall ftagger

OR

pipx uninstall ftagger
```

After running that, you will then need to remove the dotfiles located at ~/.fmdata. You may run:
```
rm -rf ~/.fmdata
```


# Usage
After installation, you should be able to run the programme from a terminal. Here is an example of what that may look like:
```
ftagger at file1.txt tag
```

Here is a breakdown of that example command:
    ftagger — the command used to invoke this programme. It is like cd, ls, cat, etc \
    at — the 'add tag' command \
    file1.txt — the target. This can be a file or a folder \
    tag — the tag to add to the target

To get help about the usage of the commands, run the following command:
```
ftagger --help
```

This will print out the table seen under the 'Help' heading. 


# Requierments
Python 3.10 and above

The project has only been tested on Linux


# Issues
If you edit any dotfiles in ~/.fmdata manually, make sure you understand how to edit the others accordingly. 

If there are any errors that mention broken dotfiles, use the 'rd' command to reset all of the dotfiles. If that doesn't fix the issue, please open an issue on the [GitHub repo](https://github.com/CharlieODwyer/ftagger.git).

If the programme crashes for any reason (you recieve a full Python error), please open an issue on the [GitHub repo](https://github.com/CharlieODwyer/ftagger.git).
