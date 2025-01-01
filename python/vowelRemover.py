myStr = input("please type in your sentence\n")
vowels = ["a","e","i","o","u"]
baseStr = "" 
for elem in myStr:
    if elem in vowels:
        baseStr = baseStr + ""
    else:
        baseStr = baseStr + elem

print("the no vowels version is: ",baseStr)