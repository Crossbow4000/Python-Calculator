firstNumber = 0
secondNumber = 0

operationIsDefined = False

firstNumberCheck = False
secondNumberCheck = False

loopRunner = 1

input("Welcome to Python Calculator, press ENTER to continue   ")

while loopRunner == 1:

    operation = input("Type one : Add  Subtract  Multiply  Divide   ");

    if operation == "add" or operation == "Add":
        while firstNumberCheck == False and secondNumberCheck == False:
            firstNumber = input("Type the first number you want to " + operation + "   ")
            try:
                firstNumberFloat = float(firstNumber)
            except:
                firstNumberCheck = False
            else:
                firstNumberCheck = True
            secondNumber = input("Type the second number   ")
            try:
                secondNumberFloat = float(secondNumber)
            except:
                secondNumberCheck = False
            else:
                secondNumberCheck = True
            if firstNumberCheck == False and secondNumberCheck == False:
                input("The inputs need to be numbers, press ENTER to try again   ")
                firstNumberCheck = False
                secondNumberCheck = False
            elif firstNumberCheck == False or secondNumberCheck == False:
                input("The inputs need to be numbers, press ENTER to try again   ")
                firstNumberCheck = False
                secondNumberCheck = False
        finalNumber = firstNumberFloat + secondNumberFloat
        finalNumberString = str(finalNumber)   
        operationIsDefined = True
        secondNumberCheck = False
        firstNumberCheck = False
        print("Your result of adding " + firstNumber + " to " + secondNumber + " was " + finalNumberString)
    elif operation == "subtract" or operation == "Subtract":
        while firstNumberCheck == False and secondNumberCheck == False:
            firstNumber = input("Type the first number you want to " + operation + "   ")
            try:
                firstNumberFloat = float(firstNumber)
            except:
                firstNumberCheck = False
            else:
                firstNumberCheck = True
            secondNumber = input("Type the second number   ")
            try:
                secondNumberFloat = float(secondNumber)
            except:
                secondNumberCheck = False
            else:
                secondNumberCheck = True
            if firstNumberCheck == False and secondNumberCheck == False:
                input("The inputs need to be numbers, press ENTER to try again   ")
                firstNumberCheck = False
                secondNumberCheck = False
            elif firstNumberCheck == False or secondNumberCheck == False:
                input("The inputs need to be numbers, press ENTER to try again   ")
                firstNumberCheck = False
                secondNumberCheck = False
        finalNumber = firstNumberFloat - secondNumberFloat
        finalNumberString = str(finalNumber)   
        operationIsDefined = True
        secondNumberCheck = False
        firstNumberCheck = False
        print("Your result of subtracting " + firstNumber + " from " + secondNumber + " was " + finalNumberString)
    elif operation == "multiply" or operation == "Multiply":
        while firstNumberCheck == False and secondNumberCheck == False:
            firstNumber = input("Type the first number you want to " + operation + "   ")
            try:
                firstNumberFloat = float(firstNumber)
            except:
                firstNumberCheck = False
            else:
                firstNumberCheck = True
            secondNumber = input("Type the second number   ")
            try:
                secondNumberFloat = float(secondNumber)
            except:
                secondNumberCheck = False
            else:
                secondNumberCheck = True
            if firstNumberCheck == False and secondNumberCheck == False:
                input("The inputs need to be numbers, press ENTER to try again   ")
                firstNumberCheck = False
                secondNumberCheck = False
            elif firstNumberCheck == False or secondNumberCheck == False:
                input("The inputs need to be numbers, press ENTER to try again   ")
                firstNumberCheck = False
                secondNumberCheck = False
        finalNumber = firstNumberFloat * secondNumberFloat
        finalNumberString = str(finalNumber)   
        operationIsDefined = True
        secondNumberCheck = False
        firstNumberCheck = False
        print("Your result of multiplying" + firstNumber + " by " + secondNumber + " was " + finalNumberString)
    elif operation == "divide" or operation == "Divide":
        while firstNumberCheck == False and secondNumberCheck == False:
            firstNumber = input("Type the first number you want to " + operation + "   ")
            try:
                firstNumberFloat = float(firstNumber)
            except:
                firstNumberCheck = False
            else:
                firstNumberCheck = True
            secondNumber = input("Type the second number   ")
            try:
                secondNumberFloat = float(secondNumber)
            except:
                secondNumberCheck = False
            else:
                secondNumberCheck = True
            if firstNumberCheck == False and secondNumberCheck == False:
                input("The inputs need to be numbers, press ENTER to try again   ")
                firstNumberCheck = False
                secondNumberCheck = False
            elif firstNumberCheck == False or secondNumberCheck == False:
                input("The inputs need to be numbers, press ENTER to try again   ")
                firstNumberCheck = False
                secondNumberCheck = False
        finalNumber = firstNumberFloat / secondNumberFloat
        finalNumberString = str(finalNumber)   
        operationIsDefined = True
        secondNumberCheck = False
        firstNumberCheck = False
        print("Your result of dividing " + firstNumber + " by " + secondNumber + " was " + finalNumberString)
    else:
        operationIsDefined = False
    
    if operationIsDefined == False:
        quit = input("That command is not defined, type QUIT to quit or press ENTER to try again   ")
    else:
        quit = input("Type QUIT if you want to quit, press ENTER if you want to continue   ")

    if quit == "QUIT" or quit == "Quit" or quit == "quit":
        break
    else:
        continue
