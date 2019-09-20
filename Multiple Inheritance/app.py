from database import Database
from admin import Admin
from user import User
a = Admin('surajkarki','suraj123',3)
u = User('suraj','password')
a.save()

print(Database.find(lambda a:a['username']=='surajkarki'))

users = [a,u]

for u in users:
    u.save()
