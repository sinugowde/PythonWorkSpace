# PythonPractice_005: List Overlap

def ListOverlap(srcList1, srcList2, dstList):
	for item in srcList1:
		if item in srcList2:
			dstList.append(item)
	return dstList

# Main Function/Method

srcList1 = []
srcList2 = []
dstList = []

lenList1 = int(input("Please enter the length of First List: "))
for item in range(0, lenList1):
	srcList1.append(int(input()))

lenList2 = int(input("Please enter the length of Second List: "))
for item in range(0, lenList2):
	srcList2.append(int(input()))
print("List1: " + str(srcList1))
print("List2: " + str(srcList2))

ListOverlap(srcList1, srcList2, dstList)

print("the Overlap List is: " + str(dstList))