# As extensões foram selecionadas através de fileinfo.com
categories: dict[str, list[str]] = {
    "Executable": ["apk", "exe", "jar", "bat", "bin", "appimage", "sh"],
    "Audio": ["mp3", "m4a", "wav"],
    "Video": ["mkv", "aep", "mp4", "m4v", "mov"],
    "Image": ["jpeg", "png", "svg"],
    "Document": ["doc", "docx", "odt", "tex", "txt", "md", "pptx", "ppt"],
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
