
# As extensões foram selecionadas através de fileinfo.com
categories: dict[str, list[str]] = {
    "Executable": ["apk", "exe", "jar", "bat", "bin", "appimage", "sh"],
    "Audio": ["mp3", "m4a", "wav"],
    "Video": ["mkv", "aep", "mp4", "m4v", "mov"],
    "Image": ["jpeg", "png", "svg"],
    "Document": ["doc", "docx", "odt", "tex", "txt", "md", "pptx", "ppt"],
    "Data": ["db", "sqlite","sql","odb","xlsx","xls","dat","csv"],
    "Compressed": ["7z", "deb", "gz", "pkg", "rar", "rpm", "tar.gz", "tar.bz2", "tar", "xapk", "zip", "zipx"],
}

def create_file_extension_dict(categories: dict[str, list[str]]) -> dict[str, str]:
    return {extension : category for category, extensions in categories.items() for extension in extensions}

if __name__ == "__main__":
    print(create_file_extension_dict(categories))
