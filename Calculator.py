# main function (ask for user input here)
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
        num1InDecimal = num1
        num2InDecimal = num2


    return

# perform addition
def addition(num1, num2):
    return num1 + num2

# perform subtraction
def subtraction(num1, num2):
    return num1 - num2

# perform multiplication
def multiplication(num1, num2):
    return num1 * num2

# perform division
def division(num1, num2):
    return num1 / num2

# get what type of operation will be done on the numbers
def getOperation():
    return 

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
        int(num_str)
        return True
    except ValueError:
        print("Please enter a valid decimal number")
        exit()

# check if entered string is a valid octal integer    
def checkIfOctal(num_str):
    try:
        int(num_str, 8)
        return True
    except ValueError:
        print("Please enter a valid octal number")
        exit()

# check if entered string is a valid hexadecimal integer
def checkIfHex(num_str):
    try:
        int(num_str, 16)
        return True
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
