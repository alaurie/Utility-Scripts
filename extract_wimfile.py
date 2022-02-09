#!/usr/bin/env python

import argparse
from pathlib import Path
import pycdlib

arg_parser = argparse.ArgumentParser(
    prog="extract-wimfile", description="Extract install.wim from Windows 10 ISO."
)

arg_parser.add_argument(
    "iso",
    metavar="my_windows.iso",
    type=str,
    help="Enter the filepath of the Windows 10 ISO to extract wim file from.",
)

arg_parser.add_argument(
    "output_path",
    metavar="my/output/path/",
    type=str,
    help="Enter the output path for the wim file.",
)

arg_parser.add_argument(
    "-f",
    "--filename",
    metavar="my_windows10.wim",
    type=str,
    default="install.wim",
    help="Enter filename for extracted wim file.",
)


def extract_wim(isofile, target_path, output_filename):
    """
    :param isofile
    """
    iso_file = Path(isofile)
    target_path = Path(target_path)
    output = Path.joinpath(target_path, output_filename)
    iso = pycdlib.PyCdlib()
    iso.open(iso_file)
    iso.get_file_from_iso(output, udf_path="/sources/install.wim")
    iso.close()


if __name__ == "__main__":
    args = arg_parser.parse_args()
    try:
        extract_wim(args.iso, args.output_path, args.filename)
    except Exception as err:
        print("There was an error extracting wim file from the ISO:", err)
