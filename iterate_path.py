#!/usr/bin/env python

# Imports
from pathlib import Path
import argparse

# Parameters
args_parser = argparse.ArgumentParser(
    prog="show-path", description="Lists all folders and files in a directory"
)

args_parser.add_argument(
    "directory",
    metavar="search/this/directory",
    type=str,
    help="Enter directory to be searched.",
)

args_parser.add_argument(
    "-p",
    "--print",
    action="store_true",
    help="Print found list of directories and files.",
    required=False,
)

# Create list objects
directories = []
files = []


# Functions
def iterate_directory(search_path):
    """Iterates through directory and adds found files or directories to their respective lists"""
    all_path_objects = search_path.glob("*")
    for path_object in all_path_objects:
        if path_object.is_dir():
            directories.append(path_object)
        else:
            files.append(path_object)


# Main
if __name__ == "__main__":
    args = args_parser.parse_args()
    iterate_directory(Path(args.directory))
    print(f"We have found {len(directories)} directories and {len(files)} files.")

    if args.print:
        if len(files) != 0:
            print("Here is a list of files found.")
            print(*files, sep="\n")
        else:
            print("No files found to print.")

        if len(directories) != 0:
            print("Here is a list of directories found.")
            print(*directories, sep="\n")
        else:
            print("No directories found to print.")
