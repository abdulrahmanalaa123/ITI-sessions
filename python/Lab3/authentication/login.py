from helpers import validators
from .user_management import check_user


def login(email,password):
    if validators.email_validation(email):
        if(validators.pass_validation(password)):
            return check_user(email=email,password=password)
        else:
            print("please enter a valid password not less than 8 characters")
    else:
        print("please enter a valid email password")
    return None