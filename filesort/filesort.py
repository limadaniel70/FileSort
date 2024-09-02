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

from config import categories, create_file_extension_dict

FILE_EXTENSIONS: dict[str, str] = create_file_extension_dict(categories)


def sort_files(directory: Path, files: list[Path]) -> None:
    for file in files:
        if file.suffix in FILE_EXTENSIONS:
            new_dir: Path = Path.joinpath(directory, FILE_EXTENSIONS[file.suffix])
            Path.mkdir(new_dir, exist_ok=True)
            try:
                file.rename(Path.joinpath(new_dir, file.name))

            except PermissionError:
                print(f"Permission deined: {PermissionError}")


def get_current_dir() -> Path:
    return Path.cwd()


def list_files(path: Path) -> list[Path]:
    return [child for child in path.iterdir()]


if __name__ == "__main__":
    current_dir = get_current_dir()
    
