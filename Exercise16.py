'''
16. Write a Python program to write a string to a buffer
and retrieve the value written, at the end discard buffer memory.

'''

import io
# Write a string to a buffer
output = io.StringIO()
output.write('Python Exercises, Practice, Solution')
# Retrieve the value written
print(output.getvalue())
print("hello world")
# Discard buffer memory
output.close()