myStr = input("please type in your sentence\n")
vowels = ["a","e","i","o","u"]
count = 0 
for elem in myStr:
    if elem in vowels:
        count = count + 1

print("the count of vowels is",count)