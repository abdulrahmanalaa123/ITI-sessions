from authentication.register import register

from authentication.login import login

register("abdelrahman AJ","b@gmail.com","123231241")
print("successfuly logged in with id of ",login("b@gmail.com","123231241"))