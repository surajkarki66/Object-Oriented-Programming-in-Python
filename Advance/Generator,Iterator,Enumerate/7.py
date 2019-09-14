# Map
# it take iterable and output a new iterable

def Lower(friends):
    return friends.lower()

friends = ['Suraj','Binish','Saman','Rojan']

friends_lower = map(Lower,friends)

print(next(friends_lower))
print(next(friends_lower))


class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    @classmethod

    def from_dict(cls,data):
        return cls(data['username'],data['password'])


users = [
    
    
    {'username': 'surajkarki','password':'suraj124'},
    {'username':'binish123','password':'hello'}

]

users = map(User.from_dict,users)

print(next(users))