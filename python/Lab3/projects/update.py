import json
from .select import select_project

def update_project(user_id,id,**arg_obj):

    valid_options = ["title","details","target","start","end"]   
    values = {key: arg_obj[key] for key in arg_obj if key in valid_options}

    if not isinstance(id,int) and not select_project(id):
        print("project doesnt exist")
        return None

    with open('projects.json','r+',encoding="utf-8") as file:
        curr_json = json.load(file) 
        final_proj = {}
        for project in curr_json["projects"]:
            if project["id"] == id:
                if project["user_id"] == user_id:
                    # here the value is update by reference manipulating original list
                    project.update(values)
                    final_proj = project
                else:
                    print("unauthorized to do such operation")
                    return None
        file.seek(0) 
        json.dump(curr_json, file,indent=4)
        print(final_proj)
        return final_proj 