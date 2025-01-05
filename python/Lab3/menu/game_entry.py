from authentication.register import register
from authentication.login import login
from .projects_menu import projects
def entry_point():
    print("Welcome to my task management app")
    print("")
    user_id = ""
    while True:
        option = input("please select one of three options:\n1) login \n2) register \n3) exit \n")
        if option.isdigit():
            match option:
                case "1":
                    email = input("please enter your email \n")
                    password = input("please enter your password \n")
                    user_id = login(email,password)
                case "2":
                    name = input("please enter your name 'FirstName LastName'\n")
                    email = input("please enter your email \n")
                    password = input("please enter your password \n")
                    user_id = register(name,email,password)
                case "3":
                    break
                case _:
                    print("please enter a number ranging from 1 to 3")
                    print("")
            if user_id:
                projects(user_id)
        else:
            print("please enter a valid number")
            print("")
