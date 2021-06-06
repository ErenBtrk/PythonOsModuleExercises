'''

3. Write a Python program to scan a specified directory and identify the sub directories and files.

'''

import os

directory = "C:\\Users\erenb\Desktop\githubprojects\PythonFundamentals"

for entry in os.scandir(directory):
    if entry.is_dir():
        type = "->dir"
    elif entry.is_file():
        type = "->file"
    elif entry.is_symlink():
        type = "->link"
    else:
        type = "->unknown"
    print(f"{entry.name}{type}")