import json
from .select import select_project
from helpers.projects_val  import parameter_validation
def update_project(user_id,id,arg_obj):

    values = parameter_validation(arg_obj)

    if not select_project(id):
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

        return final_proj 