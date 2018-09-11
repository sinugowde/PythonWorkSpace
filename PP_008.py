# PythonPractice_006: Rock Paper Scissors
#   Remember the rules:
#   - Rock beats scissors
#   - Scissors beats paper
#   - Paper beats rock

import random


def RockPaperScissor(usrSelection):
    gameOptions = ['ROCK', 'PAPER', 'SCISSOR']
    sysChoice = gameOptions[random.randint(0, 2)]

    if usrSelection in ['ROCK', 'R']:
        usrSelection = 'R'
    elif usrSelection in ["PAPER", 'P']:
        usrSelection = 'P'
    elif usrSelection in ["SCISSOR", 'S']:
        usrSelection = 'S'

    if sysChoice in ['ROCK', 'R']:
        sysChoice = 'R'
    elif sysChoice in ["PAPER", 'P']:
        sysChoice = 'P'
    elif sysChoice in ["SCISSOR", 'S']:
        sysChoice = 'S'

    print('usrSelection: %s, sysChoice: %s' % (usrSelection, sysChoice))

    if sysChoice == usrSelection:
        print('Its a Tie')
    elif sysChoice == 'R':
        if usrSelection == 'S':
            print("Sorry.. You Loose.")
        elif usrSelection == 'P':
            print("Hurray.. You Win.")
    elif sysChoice == 'S':
        if usrSelection == 'P':
            print("Sorry.. You Loose.")
        elif usrSelection == 'R':
            print("Hurray.. You Win.")
    elif sysChoice == 'P':
        if usrSelection == 'R':
            print("Sorry.. You Loose.")
        elif usrSelection == 'S':
            print("Hurray.. You Win.")
    return


def menuFunction():
    usrInput = False
    trueChoice = ['YES', 'NO', 'Y', 'N']
    while usrInput not in trueChoice:
        usrInput = input("Do you want to play again? Yes(Y)/No(N): ")
        usrInput = usrInput.upper()
        if usrInput not in trueChoice:
            print("Invalid Input.")
    return usrInput


def UserInput():
    gameOptions = ['ROCK', 'PAPER', 'SCISSOR', 'R', 'P', 'S']
    while True:
        usrCh = input("Please choose your turn: [ROCK (R), PAPER (P), SCISSOR (S)]\n ")
        usrCh = usrCh.upper()
        if usrCh in gameOptions:
            break
        else:
            print("Invalid choice")
    return usrCh


# ---------------------------------------
# Main Function/Method
# ---------------------------------------


print("Let's play ROCK, PAPER & SCISSOR Game:\n")
playOn = 'Y'

while playOn == 'Y':
    usrChoice = UserInput()
    print("usrChoice: %s" % usrChoice)
    if playOn in ['YES', 'Y']:
        print("playOn: %s" % playOn)
        RockPaperScissor(usrChoice)
    playOn = menuFunction()
    if playOn in ['NO', 'N']:
        print("\n--- Have a Nice Day ---")
        break
    else:
        if playOn not in ['YES', 'Y']:
            print("Invalid Input.\n")
