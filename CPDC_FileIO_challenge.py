with open("D:\PythonMaterials\CPDC\CPDC_FileIO_challenge.txt", 'w') as fileHandle:
    for i in range(1,13,1):
        print("%2d times 2 is %-2d" % (i, i*2), file=fileHandle)
