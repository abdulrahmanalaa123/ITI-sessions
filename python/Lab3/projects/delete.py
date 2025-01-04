import json
from .select import select_project

def delete_project(user_id,project_id):

    if not isinstance(user_id,int) and not isinstance(project_id,int) and select_project(project_id):
        print("invalid project_id")
        return None


    with open('projects.json','r+',encoding='utf-8') as file:
        curr_json = json.load(file)

        project_list = curr_json["projects"]
        for project in project_list:
            if project["id"] == project_id:
                if project["user_id"] == user_id:
                    print(f"deleted {project_id} successfully")
                else:
                    print("unauthorized to do such operation")
                    return None
        file.seek(0)  
        curr_json["projects"] = [project for project in project_list if project["id"] != project_id]
        json.dump(curr_json,file,indent=4)

        print(f"successfuly deleted project of id {project_id}")
        return project_id
