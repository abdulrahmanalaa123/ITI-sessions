import random

def dictCounter(word):
    counter = {}
    for bla in word:
       elem = bla.lower()
       if elem in counter:
           counter[elem] = counter[elem] + 1
       else:
           counter[elem] = 1
    return counter

def dictIndex(word):
    indeces = {}
    for bla in word:
        elem = bla.lower()
        if not elem in indeces:
            indeces[elem] = [index for index,value in enumerate(word) if value.lower() == elem]
    return indeces

def printState():
    pass

words = [
    "Apple", "Ocean", "Balloon", "Zebra", "Volcano", "Guitar", "Rainbow", 
    "Mountain", "Telescope", "Horizon", "Pineapple", "Adventure", "Chocolate", 
    "Elephant", "Puzzle", "Whisper", "Journey", "Lantern", "Circus", "Forest"
]

def hangman():
    selected_word = random.choice(words)
    counterDict = dictCounter(selected_word) 
    indecesDict = dictIndex(selected_word)    
    print(counterDict)
    print(indecesDict)
    name = input("please enter your name \n")

    wrongs = 0 
    board = "_"*len(selected_word)
    print("guess is ", board)

    while wrongs < 7 and (board.count("_") > 0): 
        char = input("please enter a character from the english word\n")

        if len(char) != 1:
            print("please enter a valid character")
            pass
        else:
            char = char.lower()
            if char not in counterDict:
                wrongs = wrongs + 1
                print("you have failed")
                print("try again")
            elif counterDict[char] >= 1 :
                count = counterDict[char]-1
                index = indecesDict[char][count] 
                counterDict[char] = counterDict[char] - 1
                board = board[:index] + char + board[index + 1:]
            print(board)
    if board.count("_") == 0:
        print(f"you've won {name}!!!")
        print(board)
    else:
        print("better luck next time")
    
hangman()   