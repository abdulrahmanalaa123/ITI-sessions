x = ""

while not isinstance(x,int):
    userInput = input("please enter a number: ")
    if userInput.isdigit():
        x = int(userInput)
    else:
        print("please enter simply an integer")

valueList = []
for i in range(1,x+1):
    table = []
    for j in range(1,i+1):
        table.append(i*j)
    valueList.append(table)

print("multiplication table is: ",valueList)