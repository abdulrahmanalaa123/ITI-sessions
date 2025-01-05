import datetime
from projects.create import create_project
from projects.select import select_project 
from projects.select import query_project 
from projects.delete import delete_project 

from projects.update import update_project
from helpers.projects_val import parameter_validation
from menu.game_entry import entry_point

if __name__ == "__main__":
    entry_point()
# datetime.datetime.now().strftime('%Y-%m-%d')
#create_project(user_id=user_id,title="Test_Project",details="blablalbalblabl",target=25000,date="wahtever")
#select_project(10)
#query_project("Test_Project")
#update_project(user_id=user_id,id=10,title="new title testing update",details="new_details")
# deleting is bugged because it overwrites the current cursor and file aftere deletion is smaller than 
#delete_project(user_id=user_id,project_id=12)

