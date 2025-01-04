import json

def email_already_exists (email):
    with open("users.json","r",encoding="utf-8") as file:
        json_file=json.load(file)
        return any([email in user["email"] for user in json_file["users"]])

# email, name , password
def user_add(**user_obj):
    with open('users.json','r+',encoding="utf-8") as file:
        curr_json = json.load(file)
        user_obj["id"] = curr_json["latest_user_id"] + 1
        #increasing the id to determine the latest user id 
        if email_already_exists(user_obj["email"]):
            print("email already exists please try another email or login and use forgot passowrd")
            return None

        curr_json["latest_user_id"] = curr_json["latest_user_id"] + 1
        curr_json["users"].append(user_obj)
        #return the cursor back to 0 because reading exhausted the cursor
        file.seek(0)
        json.dump(curr_json,file,indent=4)
        return user_obj["id"] 

# email, password
def check_user(**user_obj):
    with open('users.json','r',encoding='utf-8') as file:
        json_file = json.load(file)
        for user in json_file["users"]:
            if (user["email"] == user_obj["email"]) and (user["password"] == user_obj["password"]):
                return user["id"]
        print("email doesnt exist or wrong password")
        return None
