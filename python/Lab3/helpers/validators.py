import re


def name_validation (name):
   #name cant contain special characters
   return bool(re.fullmatch(r'[a-zA-Z]{2,25}\s[a-zA-Z]{2,25}',name))

def pass_validation(passwd):
   #minimum 8 letters password 
   return bool(re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}',passwd))
   
def email_validation(email):
   email_reg = r'[A-Za-z0-9.%_+-]+\@[A-Za-z0-9]+\.[A-Za-z0-9]+'
   return bool(re.fullmatch(email_reg,email))
   
def phone_validation(phone):
   return bool(re.fullmatch(r'^(010|011|012)+[0-9]{8}',phone))
   


