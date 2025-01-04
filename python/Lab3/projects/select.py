import json

def select_project(project_id):
    if not isinstance(project_id,int):
        print("invalid project_id")
        return None
    with open('projects.json','r+',encoding='utf-8') as file:
        curr_json = json.load(file)
        if project_id > curr_json["latest_project_id"]:
            print("project doesnt exist")
            return None
        else:
            project =  [project for project in curr_json["projects"] if project_id == project["id"] ]
            print(f"project is {project}")
            if len(project):
                return project[0]
            return None


def query_project(title):
    with open('projects.json','r+',encoding='utf-8') as file:
        curr_json = json.load(file)
        projects =  [project for project in curr_json["projects"] if title.lower() == project["title"].lower() ]
        print(f"projects are {projects}")
        if len(projects):
            return projects
        return None

