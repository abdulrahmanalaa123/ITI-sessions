from authentication.register import register
import datetime
from authentication.login import login
from projects.create import create_project
from projects.select import select_project 
from projects.select import query_project 
from projects.delete import delete_project 

from projects.update import update_project

register("abdelrahman AJ","bawdlqq@gmail.com","123231241")
user_id = login("bawdlqq@gmail.com","123231241")
#TODO 
#menu
# projects parameter validation (take in dict and validate all to reference)
# deletion with updating bug idk what yet but let it be
print("successfuly logged in with id of ", user_id)
# datetime.datetime.now().strftime('%Y-%m-%d')
create_project(user_id=user_id,title="Test_Project",details="blablalbalblabl",target=25000,date="wahtever")
select_project(3)
query_project("Test_Project")
update_project(user_id=user_id,id=3,title="new title testing update",details="new_details")
delete_project(user_id=user_id,project_id=8)
