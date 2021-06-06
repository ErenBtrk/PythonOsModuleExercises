'''

9. Write a Python program to retrieve the current working
directory and change the dir (moving up one).
 
'''

import os

print(os.getcwd())
os.chdir("..")
print(os.getcwd())