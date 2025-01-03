inputStr = ""

numList = []
while inputStr != "done":
    inputStr = input("please enter a valid number \n") 
    if inputStr.isdigit():
        numList.append(int(inputStr))
    elif inputStr != "done":
        print("enter a valid number and only 1")

total = sum(numList)
print(f"total sum is {total} and count is {len(numList)} and avg is {total/len(numList)}")