inputVal = input("please enter a sentence\n")

indexList = [index for index,elem in enumerate(inputVal) if elem == "i" ]

print("indeces of cases where i happened is: ", indexList)