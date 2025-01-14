import json
from .select import select_project

def delete_project(user_id,project_id):

    if not select_project(project_id): 
        print("project doesnt exist")
        return None


    with open('projects.json','r+') as file:
        curr_json = json.load(file)

        for project in curr_json["projects"]:
            if project["id"] == project_id:
                if project["user_id"] != user_id:
                    print("unauthorized to do such operation")
                    return None

        vals = [project for project in curr_json["projects"] if project["id"] != project_id]
        curr_json["projects"] = vals
        file.seek(0)
        # there was an error where writing would overwrite the file leaving the last element breaking the json format
        # another method would be to open the file as simply write and write to it but that would require to save the json
        # as a local to the function and alot of editing and i didnt wnat to do that
        file.write(json.dumps(curr_json,indent=4))
        #truncate specifies that the file size is where the current position is when not given an argument
        file.truncate()
        print(f"deleted {project_id} successfully")
        return project_id
   