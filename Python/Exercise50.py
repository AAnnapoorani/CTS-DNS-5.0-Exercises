# Exercise 50

import shutil
import os

copied_files = set()

source_files = [
    "file1.txt",
    "file2.txt"
]

backup_folder = "backup"

os.makedirs(backup_folder, exist_ok=True)

for file in source_files:

    try:

        if file not in copied_files:

            shutil.copy(
                file,
                backup_folder
            )

            copied_files.add(file)

            print(f"Copied: {file}")

    except FileNotFoundError:
        print(f"{file} not found")

    except PermissionError:
        print(f"No permission for {file}")

