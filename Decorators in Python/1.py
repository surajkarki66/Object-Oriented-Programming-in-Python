'''  
Decorators: they are higher order functions which takes other function
as an argument and return a function

'''


user =   {'username':'suraj','access_level':'admin'}


def user_has_permission(func):
    if user.get('access_level') == 'admin':
        return func

    raise RuntimeError

def my_function():
    return  'password is 12345'

my_secure_function = user_has_permission(my_function)
print(my_secure_function())
