from datetime import datetime

def date_parser(date):
    try:
        parsed = datetime.strptime(date, '%Y%m%d')
        return parsed
    except:
        print(f"invalid date string YYYYmmdd {date}\n")
        return None

def str_parser(inputStr):
    if inputStr != "":
        return inputStr
    else:
        print("cant have an empty string\n")
        return None

def int_parse(intStr):
    if intStr.isdigit():
        return int(intStr)
    else:
        print("please enter a valid number\n")
        return None

def parameter_validation(params):
    valid_options = ["title","details","target","start","end"]   
    values = {key: params[key] for key in params if key in valid_options}
    return values
