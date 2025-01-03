def reverse_str(inputStr):
    if isinstance(inputStr,str):
        return inputStr[::-1]
    return ""

inputStr = input("please enter a string \n")

print("reversed str is:",reverse_str(inputStr))