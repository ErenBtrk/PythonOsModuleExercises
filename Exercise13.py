'''

13. Write a Python program to join one or more path components
together and split a given path in directory and file.
 
'''

import os
path = "C:\\Users\erenb\Desktop\githubprojects\PythonOsModuleExercises\testpath"
print("Original path:")
print(path)
print("\nDir and file name of the said path:")
print(os.path.split(path))
print("\nJoin one or more path components together:")
print(os.path.join(path,'a.txt'))