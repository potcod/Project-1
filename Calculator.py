# main function (ask for user input here)
def main():
    numberType = getNumberType()
    number1 = getInputs(numberType)
    number2 = getInputs(numberType)

    return

# perform addition
def addition(num1, num2):
    return

# perform subtraction
def subtraction(num1,num2):
    return

# perform multiplication
def multiplication(num1, num2):
    return

# perform division
def division(num1,num2):
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
        numString = str(input("Enter number: "))
        checkIfDecimal(numString)
    elif numberType == 2:
        numString = str(input("Enter number: "))
        checkIfOctal(numString)
    elif numberType == 3:
        numString = str(input("Enter number: "))
        checkIfHex(numString)
    return numString

# check if entered string is a valid decimal integer
def checkIfDecimal(num_str):
    try:
        int(num_str)
        return True
    except ValueError:
        print("Enter a valid decimal number")
        exit()
    
# check if entered string is a valid octal integer    
def checkIfOctal(num_str):
    try:
        int(num_str, 8)
        return True
    except ValueError:
        print("Enter a valid octal number")
        exit()

# check if entered string is a valid hexadecimal integer
def checkIfHex(num_str):
    try:
        int(num_str, 16)
        return True
    except ValueError:
        print("Enter a valid hexadecimal number")
        exit()

#converts the octal number to decimal
def getOctalNumber(string):
    return int(string,8)

#converts the hexadecimal number to decimal
def getHexNumber(string):
    return int(string,16)

if __name__ == '__main__':
    main()
