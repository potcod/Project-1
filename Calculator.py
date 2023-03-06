# main function (ask for user input here)
def main():
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

# check if entered string is a valid decimal integer
def checkIfDecimal(num_str):
    try:
        int(num_str)
        return True
    except ValueError:
        return False
    
# check if entered string is a valid octal integer    
def checkIfOctal(num_str):
    try:
        int(num_str, 8)
        return True
    except ValueError:
        return False

# check if entered string is a valid hexadecimal integer
def checkIfHex(num_str):
    try:
        int(num_str, 16)
        return True
    except ValueError:
        return False

#converts the octal number to decimal
def getOctalNumber(string):
    return int(string,8)

#converts the hexadecimal number to decimal
def getHexNumber(string):
    return int(string,16)

if __name__ == '__main__':
    main()
