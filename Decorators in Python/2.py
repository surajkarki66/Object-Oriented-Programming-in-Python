import functools

user =   {'username':'suraj','access_level':'admin'}


def user_has_permission(func):

    @functools.wraps(func)
    def secure_func():                                    # Wrapping function
            
        if user.get('access_level') == 'admin':
            return func()
        raise RuntimeError

    return secure_func

    

@user_has_permission            # it automatically called the my_function
def my_function():
    return  'password is 12345'

print(my_function())
print(my_function.__name__)

