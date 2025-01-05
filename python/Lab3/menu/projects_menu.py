from helpers.projects_val import str_parser
from helpers.projects_val import int_parse
from helpers.projects_val import date_parser

from projects.create import create_project
import projects.select as select
from projects.delete import delete_project

def projects(user_id):
    user = user_id 

    parameters = {"title":(lambda x: str_parser(x)),
                  "details":(lambda x: str_parser(x)),
                  "target":(lambda x: int_parse(x)),
                  "start":(lambda x: date_parser(x)),
                  "end":(lambda x: date_parser(x))}

    
    while user:
        option = input("please select one of three options:\n1) create a project\n2) list projects\
                   \n3) query projects with title\n4) query project with date\n5) delete project\n6) update project\n7) list all projects\n8) logout\n")
        if option.isdigit():
            match option:
                case "1":
                    input_dict = {}
                    valid = True
                    for key in parameters:
                        input_dict[key] = parameters[key](input(f"Please enter the project's {key}\n"))
                        if not input_dict[key]:
                            valid = False
                            break
                    if valid:
                        create_project(user_id=user,project_obj=input_dict)
                case "2":
                    projects = select.select_your_projects(user)
                    if len(projects):
                        print(projects)
                    else:
                        print("create some projects for us :D\n")
                case "3":
                    title = parameters["title"](input("please enter your title \n"))
                    if title:
                        select.query_project(title)
                case "4":
                    pass
                case "5":
                    project_id = int_parse(input("please enter your id\n"))
                    if project_id:
                        delete_project(user_id=user,project_id=project_id) 
                case "6":
                    input_dict = {}
                    valid = True
                    for key in parameters:
                        input_dict[key] = parameters[key](input(f"Please enter the project's {key}\n"))
                        if not input_dict[key]:
                            valid = False
                            break
                    if valid:
                        create_project(user_id=user,project_obj=input_dict)
                case "7":
                    projects = select.select_projects()
                    print(projects)
                case "8":
                    user = None
                    break
                case _:
                    print("please enter a number ranging from 1 to 8")
                    print("")
        else:
            print("please enter a valid number")