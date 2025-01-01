x = ""

while not isinstance(x,int):
    userInput = input("please enter a number: ")
    if userInput.isdigit():
        x = int(userInput)
    else:
        print("please enter simply an integer")

for i in range(1,x+1):
    line = " "*(x-i)+"*"*i
    print(line)
