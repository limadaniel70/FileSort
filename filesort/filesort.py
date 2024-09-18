#!/usr/bin/env python
# MIT License
#
# Copyright (c) 2024 Daniel Lima
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pathlib import Path

from .config import CATEGORIES, create_file_extension_dict

FILE_EXTENSIONS: dict[str, str] = create_file_extension_dict(CATEGORIES)


def sort_files(directory: Path) -> None:
    """
    Organizes files in the specified directory into subdirectories based on their file extensions.

    This function scans the provided directory, and for each file with a recognized extension (as defined
    in the FILE_EXTENSIONS dictionary), it creates (if necessary) a subdirectory named after the file's
    extension category and moves the file into that subdirectory. It handles permission errors if the file
    cannot be moved.

    Args:
        directory (Path): The directory containing the files to be organized. This should be a
                        `Path` object representing a valid directory path.
    Raises:
        PermissionError: If the function does not have permission to move a file, it will print
                        a message indicating the error.
    """
    organized_files: int = 0

    for file in directory.iterdir():
        if file.suffix in FILE_EXTENSIONS:
            new_dir: Path = Path.joinpath(directory, FILE_EXTENSIONS[file.suffix])
            Path.mkdir(new_dir, exist_ok=True)
            try:
                file.rename(Path.joinpath(new_dir, file.name))
                organized_files += 1
            except PermissionError:
                print(f"Permission deined: could not move the file {file}.")

    print(f"Files organized: {organized_files}")


if __name__ == "__main__":
    sort_files(Path.cwd())
