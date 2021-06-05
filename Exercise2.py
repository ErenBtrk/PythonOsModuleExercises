'''
2. Write a Python program to list only directories, files
and all directories, files in a specified path. 

'''

import os
pathname = os.getcwd()

print("Only directories:")
print([ name for name in os.listdir(pathname) if os.path.isdir(name) ])

print("\nOnly files:")
print([ name for name in os.listdir(pathname) if os.path.isfile(name) ])

print("\nAll directories and files :")
print([ name for name in os.listdir(pathname)])

