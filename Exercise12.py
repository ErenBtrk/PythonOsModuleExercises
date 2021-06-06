'''
12. Write a Python program to test whether a given path exists or not.
If the path exist find the filename and directory portion of the said path.

'''

import os

path1 = "C:\\Users\erenb\Desktop\githubprojects\PythonFundamentals"
path2 = "C:\\Users\erenb\Desktop\githubprojects\JAVA"

if(os.path.exists(path1)):
    print(f"{path1} EXISTS")
    print(os.path.basename(path1))
    print(os.path.dirname(path1))
else:
    print(f"{path1} DOES NOT EXISTS.")

if(os.path.exists(path2)):
    print(f"{path2} EXISTS")
    print(os.path.basename(path2))
    print(os.path.dirname(path2))
else:
    print(f"{path2} DOES NOT EXIST.")