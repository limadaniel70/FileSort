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

# As extensões foram selecionadas através de fileinfo.com
categories: dict[str, list[str]] = {
    "Executable": ["apk", "exe", "jar", "bat", "bin", "appimage", "sh"],
    "Audio": ["mp3", "m4a", "wav"],
    "Video": ["mkv", "aep", "mp4", "m4v", "mov"],
    "Image": ["jpeg", "png", "svg", "gif", "webp"],
    "Document": ["doc", "docx", "odt", "tex", "txt", "md", "pptx", "ppt", "pdf"],
    "Data": ["db", "sqlite", "sql", "odb", "xlsx", "xls", "dat", "csv"],
    "Compressed": [
        "7z",
        "deb",
        "gz",
        "pkg",
        "rar",
        "rpm",
        "tar.gz",
        "tar.bz2",
        "tar",
        "xapk",
        "zip",
        "zipx",
    ],
}


def create_file_extension_dict(file_categories: dict[str, list[str]]) -> dict[str, str]:
    """
    Formata as categorias em um dicionário que segue este padrão:

    "rpm" : "Compressed",
    "png" : "Image",
    ...

    Args:
        categories (dict[str, list[str]]): Um dicionário que define as categorias
        para cada tipo de arquivo.

    Returns:
        dict[str, str]: Um dicionário em que as chaves são as extensões dos
        arquivos e os valores são a sua categoria.

    """
    return {
        extension: category
        for category, extensions in file_categories.items()
        for extension in extensions
    }


if __name__ == "__main__":
    print(create_file_extension_dict(categories))
