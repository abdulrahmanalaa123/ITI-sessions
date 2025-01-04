import json

def create_project(**project_obj):
    
    #TODO
    # create parameter validation
    with open('projects.json','r+',encoding='utf-8') as file:
        print(project_obj)
        curr_json = json.load(file)
        project_obj["id"] = curr_json["latest_project_id"] + 1
        #increasing the id to determine the latest user id 
        curr_json["latest_project_id"] = curr_json["latest_project_id"] + 1
        curr_json["projects"].append(project_obj)
        #return the cursor back to 0 because reading exhausted the cursor
        #to wrtie from the beginning of the file
        file.seek(0)
        json.dump(curr_json,file,indent=4)
        return project_obj["id"] 

