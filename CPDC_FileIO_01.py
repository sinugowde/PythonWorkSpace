# fileHandle = open("D:\PythonMaterials\CPDC\sample.txt", 'r')
# for line in fileHandle:
#     print(line, end='')
# fileHandle.close()

# File handling using "with" keyword:
# by using "with" statement we don't need
# to take of closing the file @ the end of our file usage.

# with open("D:\PythonMaterials\CPDC\sample.txt", 'r') as fileHandle:
#     for line in fileHandle:
#         print(line, end='')

# with open("D:\PythonMaterials\CPDC\sample.txt", 'r') as fileHandle:
#     for line in fileHandle:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("D:\PythonMaterials\CPDC\sample.txt", 'r') as fileHandle:
#     line = fileHandle.readline()
#     while line:
#         print(line, end='')

with open("D:\PythonMaterials\CPDC\sample.txt", 'r') as fileHandle:
    lines = fileHandle.readlines()
    print(lines, end='')
for line in lines:
    print(line, end='')

