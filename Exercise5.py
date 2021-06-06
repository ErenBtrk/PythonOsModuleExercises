'''
5. Write a Python program to get the size, permissions, owner, device,
created, last modified and last accessed date time of a specified path.

'''

import os
import sys
import time

directory = "C:\\Users\erenb\Desktop\githubprojects\PythonFundamentals"

print("Size of the path : ",os.path.getsize(directory)/1024)
print('Permissions:', oct(os.stat(directory).st_mode))
print('Owner:', os.stat(directory).st_uid)
print('Device:', os.stat(directory).st_dev)
print('Created     :', time.ctime(os.stat(directory).st_ctime))
print('Last modified:', time.ctime(os.stat(directory).st_mtime))
print('Last accessed:', time.ctime(os.stat(directory).st_atime))