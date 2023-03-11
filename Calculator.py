# main function (ask for user input here)1
def main():
    numberType = getNumberType()
    print("Enter first number")
    num1 = getInputs(numberType)
    print("Enter second number")
    num2 = getInputs(numberType)

    if (numberType == 2):
        num1InDecimal = getOctalNumber(num1)
        num2InDecimal = getOctalNumber(num2)
    elif (numberType == 3):
        num1InDecimal = getHexNumber(num1)
        num2InDecimal = getHexNumber(num2)
    else:
        num1InDecimal = int(num1)
        num2InDecimal = int(num2)

    operationType = getOperation()
    performOperation(num1InDecimal, num2InDecimal, operationType)

    return


# perform addition
def addition(num1, num2):
    print("The two numbers added together =", num1 + num2)


# perform subtraction
def subtraction(num1, num2):
    print("The two numbers subtracted = ", num1 - num2)


# perform multiplication
def multiplication(num1, num2):
    print("The two numbers multiplied together = ", num1 * num2)


# perform division
def division(num1, num2):
    print("The two numbers divided = ", num1 / num2)


# get what type of operation will be done on the numbers
def getOperation():
    print("What type of operation would you like to do?\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")
    operationType = int(input("Operation type: "))
    while True:
        if (operationType == 1) or (operationType == 2) or (operationType == 3) or (operationType == 4):
            return operationType
        else:
            print(
                "Please select a valid option.\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")
            operationType = int(input("Operation type: "))


# performs the operation on the two numbers
def performOperation(num1, num2, operationNumber):
    if (operationNumber == 1):
        addition(num1, num2)
    elif (operationNumber == 2):
        subtraction((num1, num2))
    elif (operationNumber == 3):
        multiplication(num1, num2)
    else:
        division(num1, num2)


# get what type of number is being used for calculations
def getNumberType():
    print("What type of numbers do you want to calculations on?\n1: Decimal\n2: Octal\n3: Hexadecimal")
    type = int(input("Number type: "))
    while True:
        if (type == 1) or (type == 2) or (type == 3):
            return type
        else:
            print("Please select a valid option.\n1: Decimal\n2: Octal\n3: Hexadecimal")
            type = int(input("Number type: "))


# get input numbers based on the number type
def getInputs(numberType):
    if numberType == 1:
        numString = str(input(""))
        checkIfDecimal(numString)
    elif numberType == 2:
        numString = str(input(""))
        checkIfOctal(numString)
    elif numberType == 3:
        numString = str(input(""))
        checkIfHex(numString)
    return numString


# check if entered string is a valid decimal integer
def checkIfDecimal(num_str):
    try:
        if num_str.isnumeric():
            return True
        else:
            raise ValueError()
    except ValueError:
        print("Please enter a valid decimal number")
        exit()


# check if entered string is a valid octal integer
def checkIfOctal(num_str):
    try:
        if num_str.startswith("0o"):
            return True
        else:
            raise ValueError()
    except ValueError:
        print("Please enter a valid octal number")
        exit()


# check if entered string is a valid hexadecimal integer
def checkIfHex(num_str):
    try:
        if num_str.startswith("0x"):
            return True
        else:
            raise ValueError()
    except ValueError:
        print("Please enter a valid hexadecimal number")
        exit()


# converts the octal number to decimal
def getOctalNumber(string):
    return int(string, 8)


# converts the hexadecimal number to decimal
def getHexNumber(string):
    return int(string, 16)


if __name__ == '__main__':
    main()
