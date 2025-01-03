def checkString(inputStr):
    return name and (not any(char.isdigit() for char in inputStr))

def checkValidExp(inputStr):
    rejected = " --\`\"\'<>^~"
    return not any(char in rejected for char in inputStr)

def checkEmail(inputStr):
    splittedStr = inputStr.split("@")

    if((len(splittedStr) != 2)):
       return False

    domain = splittedStr[1].split('.')
    if(len(domain) != 2):
        return False
    else:
        return (checkValidExp(splittedStr[0]) and 
        checkValidExp(splittedStr[1]) and
        checkValidExp(domain[0]) and
        checkValidExp(domain[1]))

name = input("please enter your name \n")

if checkString(name):
    email = input("please enter your email\n")
    if checkEmail(email):
        print("all valid thanks!")
    else:
        print("invalid email")
else:
    print("invalid name")    
