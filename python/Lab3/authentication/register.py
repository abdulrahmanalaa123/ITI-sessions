from helpers import validators
from .user_management import user_add


def register(name,email,password):
    if validators.name_validation(name): 
        if validators.email_validation(email):
            if validators.pass_validation(password):
               return user_add(email=email,name=name,password=password) 
            else:
                print("please a valid password at least containing 8 characters")
        else:
            print("please enter a valid email address")
    else:
        print("please enter your first name and last name")
    return None

