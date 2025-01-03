def longestSubstr(inputStr):
    firstPointer = 0
    secondPointer = 0
    longest = [0,0,0]
    curr = 0 
    prev = ""
    for index, elem in enumerate(inputStr):
        if(elem.lower() >= prev):
            secondPointer = index 
            curr = curr + 1
            if(curr > longest[0]):
                longest[0] = curr
                longest[1] = firstPointer
                longest[2] = secondPointer
        else:
            firstPointer= index
            secondPointer = index 
            curr = 0 
        prev = elem.lower()
    return longest 

inputStr = input("please enter your string: \n")
length,startPos,endPos = longestSubstr(inputStr)

print(f"start {startPos} , end {endPos}, length {length} ")
print("longest substr is: ", inputStr[startPos:endPos+1], "of length of", length)
 