import os

def scan_files(folder_path):
    files = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            files.append((filename, size))

    return files