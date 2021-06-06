'''
17. Write a Python program to run an 
operating system command using the os module.

'''

import os
if os.name == "nt":
   command = "dir"
else:
   command = "ls -l"
   
os.system(command)