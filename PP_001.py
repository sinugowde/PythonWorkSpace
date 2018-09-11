# PythonPractice_001: Character Input

import datetime
def YourAge(age):
    today = datetime.datetime.now()
    currYear = (today.timetuple())[0]
    yourDoB = (currYear - age) + 100
    return yourDoB

# Main Function/Method

yourName = input("Please Enter Your Name: ")
yourAge = int(input("Please Enter your Age: "))
yourYoB = YourAge(yourAge)
print('Dear ' + yourName + '! You will turn 100 year in the year: '\
      + str(yourYoB))
