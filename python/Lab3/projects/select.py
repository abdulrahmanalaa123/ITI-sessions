import json

def select_project(project_id):

    with open('projects.json','r',encoding='utf-8') as file:
        curr_json = json.load(file)
        if project_id > curr_json["latest_project_id"]:
            print("project doesnt exist")
            return None
        else:
            project =  [project for project in curr_json["projects"] if project_id == project["id"] ]
            if len(project):
                return project[0]

        print("project doesnt exist")
        return None

def select_your_projects(user_id):
    with open('projects.json','r',encoding='utf-8') as file:
        curr_json = json.load(file)
        projects =  [project for project in curr_json["projects"] if user_id == project["user_id"] ]
        return projects

def select_projects():
    with open('projects.json','r',encoding='utf-8') as file:
        curr_json = json.load(file)
        return curr_json["projects"] 

def query_project(title):
    with open('projects.json','r',encoding='utf-8') as file:
        curr_json = json.load(file)
        projects =  [project for project in curr_json["projects"] if title.lower() in project["title"].lower() ]
        if len(projects):
            return projects
        return None
