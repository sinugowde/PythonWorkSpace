# PythonPractice_003: List Less Than N
def ListLessThanN(srcList, dstList, choiceNum):
	for item in srcList:
		if item <= choiceNum:
			#print(" - " + str(item))
			dstList.append(item)

# Main Function/Method

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
srcList = []
dstList = []

lenList = int(input("Please Enter the length of the List: "))
print("Please Enter elements of the List: ")
for i in range(0, lenList):
	srcList.append(int(input()))
print(srcList)
choiceNum = int(input("Please enter the Number below which you want to print the list: "))
ListLessThanN(srcList, dstList, choiceNum)
print("\n Your filtered List: ")
print(dstList)
