executable_files: dict[str, str] = {
    "apk": "Executable",
    "exe": "Executable",
    "jar": "Executable",
    "bat": "Executable",
    "bin": "Executable",
    "appimage": "Executable",
    "sh": "Executable",
}

media_files: dict[str, str] = {
    "mp3": "Audio",
    "m4a": "Audio",
    "wav": "Audio",
    "mkv": "Video",
    "aep": "Video",
    "mp4": "Video",
    "m4v": "Video",
    "mov": "Video",
    "jpeg": "Image",
    "png": "Image",
    "svg": "Image",
}

text_document_files: dict[str, str] = {
    "doc": "Document",
    "docx": "Document",
    "odt": "Document",
    "tex": "Document",
    "txt": "Document",
    "md": "Document",
    "pptx": "Document",
    "ppt": "Document",
}

data_files: dict[str, str] = {
    "db": "Data",
    "sqlite": "Data",
    "sql": "Data",
    "odb": "Data",
    "xlsx": "Data",
    "xls": "Data",
    "dat": "Data",
    "csv": "Data",
}

compressed_files: dict[str, str] = {
    "7z": "Compressed",
    "deb": "Compressed",
    "gz": "Compressed",
    "pkg": "Compressed",
    "rar": "Compressed",
    "rpm": "Compressed",
    "tar.gz": "Compressed",
    "tar.bz2": "Compressed",
    "tar": "Compressed",
    "xapk": "Compressed",
    "zip": "Compressed",
    "zipx": "Compressed",
}

files: dict[str, str] = executable_files | media_files | text_document_files | data_files | compressed_files
