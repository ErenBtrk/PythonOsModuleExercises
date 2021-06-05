'''
1. Write a Python program to get the name of the operating system 
(Platform independent), information of current operating system,
current working directory, print files and directories in the
current directory and raises error in the case of invalid or
inaccessible file names and paths.

'''

import os
import platform



print(f"Operating system = {os.name}")

print(f"Information about operating system = {platform.uname()}")

print(f"Current working directory = {os.getcwd()}")

print(f"Files and directories in the current directory :")
print(os.listdir())

filename = "text.txt"
result = os.path.exists(filename)
if(result):
    print(f"{filename} file exists.")
else:
    print(f"{filename} file doesnt exist.")