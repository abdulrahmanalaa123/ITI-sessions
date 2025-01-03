def numberChecker(*args):
    numList = []
    print("args is ", args)
    for elem in args:
        if elem.isdigit():
            numList.append(int(elem))
    return numList

def generator(length,start):
    if isinstance(length,int) and isinstance(start,int):
        return list(range(start,(start+length+1)))
    return [];

if __name__ == "__main__":
    bla = input("please enter valid 2 numbers space seperated \n").split(" ")
    #spread operator using *  (list unpacking)
    nums = numberChecker(*bla)
    if(len(nums) >= 2):
        print("this is the returned list",generator(nums[0],nums[1]))
    else:
        print("sorry you haven't entered enough numbers") 


