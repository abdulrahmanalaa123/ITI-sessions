def correct(l):
    digits = []
    for elem in l:
        if(elem.isdigit()):
            digits.append(int(elem))
    return digits

inputArray = input("enter your numbers seperated by a space\n").split()

numList = correct(inputArray)

if len(numList) < 5:
    print("not enough numbers please enter again a minimum of 5")
else:
    print("sorted List:",sorted(numList))
    print("reverse sorted List:",sorted(numList,reverse=True))