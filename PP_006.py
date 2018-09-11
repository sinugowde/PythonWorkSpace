# PythonPractice_006: Polindrome

def checkPolindrome(stringVar):
	for i in range(0, len(stringVar)//2):
		if stringVar[i] != stringVar[-i-1]:
			resVar = False
			break
		resVar = True
	return resVar

# Main Function/Method

stringVar = input()
resVar = checkPolindrome(stringVar)

if resVar:
	print("the Entered string: " + stringVar + ", is a POLINDROME")
else:
	print("the Entered string: " + stringVar + ", is not a POLINDROME")