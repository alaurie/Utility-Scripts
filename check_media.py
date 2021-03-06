#!/usr/bin/env python
# -*- coding utf-8 -*-
import argparse
from pathlib import Path
from os import chdir
import ffmpeg

args_parser = argparse.ArgumentParser(
    prog="check-media", description="Directory of media files to process."
)

args_parser.add_argument(
    "directory",
    metavar="directory",
    type=str,
    help="Enter the directory to search for media files to process.",
)


def get_files(extension):
    """Retrieve all files with specified extension"""
    all_files = []
    for ext in extension:
        all_files.extend(Path(args.directory).rglob(ext))
    return all_files


def process_files(file_list):
    """Check files passed in to see if they are .avi or audio is not ac3 and recode as required"""
    for file in file_list:
        # Change to file dir and generate probe info and new_filename
        chdir(file.parent)
        info = ffmpeg.probe(file, select_streams="a:0")
        new_filename = str(file.name).split(".", maxsplit=1)[0] + ".mp4"

        if file.suffix == ".avi":
            try:
                (
                    ffmpeg.input(file.name)
                    .output(new_filename, acodec="ac3", vcodec="copy")
                    .run(capture_stdout=True, capture_stderr=True)
                )
                Path.unlink(file)
            except ffmpeg.Error as error:
                print(error.stderr)
                continue
        elif info["streams"][0]["codec_name"] != "ac3":
            try:
                (
                    ffmpeg.input(str(file.name))
                    .output(new_filename, acodec="ac3", vcodec="copy")
                    .run(capture_stdout=True, capture_stderr=True)
                )
                Path.unlink(file)
            except ffmpeg.Error as error:
                print(error.stderr)
                continue

        else:
            continue


if __name__ == "__main__":
    args = args_parser.parse_args()
    files = get_files(("*.mkv", "*.mp4", "*.avi"))
    process_files(files)
