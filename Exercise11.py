'''

11. Write a Python program to iterate over a root level path and print
all its sub-directories and files, also loop over specified dirs and files.

'''

import os
print('Loop over dirs and files:')
path = 'C:\\Users\erenb\Desktop\githubprojects\PythonFundamentals'
for root, dirs, files in os.walk(path):
       print(root)
       for _dir in dirs:
           print(_dir)
       for _file in files:
           print(_file)