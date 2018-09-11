# PythonPractice_002: Odd Or Even

def OddOrEven(num):
	if(num % 2):
		typeNum = False
	else:
		typeNum = True
	return typeNum

# Main Function/Method

usrNum = int(input("Please Your Number: "))
usrNumType = OddOrEven(usrNum)
if(usrNumType == True):
	print("You have entered an Even Number")
else:
	print("You have entered an Odd Number")