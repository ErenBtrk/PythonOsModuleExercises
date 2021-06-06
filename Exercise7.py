'''
7. Write a Python program to create a file and write some text and rename the file name.

'''

import os

with open("text.txt","w") as file:
    file.write("Hello World.How are you?")

os.rename("text.txt","newtext.txt")
