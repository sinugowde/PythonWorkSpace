# PythonPractice_004: Divisors

def findDivisor(num):
	tempList = []
	for i in range(2, num+1):
		if (num % i) == 0:
			tempList.append(i)
	return tempList

# Main Function/Method

num = int(input("Please enter the number: "))
myList = findDivisor(num)
print(myList)