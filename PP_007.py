# PythonPractice_006: List Comprehensions

def  listComprehensions(srcList, dstList):
	for i in srcList:
		if i % 2 == 0:
			dstList.append(i)
	return dstList

# Main Function/Method

srcList = []
dstList = []
lenList = int(input("Please length of the List: "))
for i in range(0, lenList):
	srcList.append(int(input()))

print("your List: " + str(srcList))
listComprehensions(srcList, dstList)
print("the Even Numbers from your List: " + str(dstList))