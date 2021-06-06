'''
10. Write a python program to access environment
variables and value of the environment variable.

'''
import os
print("Access all environment variables:")
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
print("Access a particular environment variable:")
print(os.environ['temp'])
print('*----------------------------------*')
print(os.environ['path'])
print('*----------------------------------*')
print('Value of the environment variable key:')
print(os.getenv('JAVA_HOME'))
print(os.getenv('PYTHONPATH'))