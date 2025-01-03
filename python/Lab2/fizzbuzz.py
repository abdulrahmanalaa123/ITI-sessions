def fizzBuzz(number):
    if number.isdigit():
        number = int(number)
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print("bla")
    else:
        print("Not a Number!")

number = input("please enter a nubmer\n")

fizzBuzz(number)