# To make it generic
import functools

user =   {'username':'suraj','access_level':'admin'}


def user_has_permission(func):

    @functools.wraps(func)
    def secure_func(*args,**kwargs):                                    # Wrapping function
            
        if user.get('access_level') == 'admin':
            return func(*args,**kwargs)
        raise RuntimeError

 
    return secure_func


@user_has_permission              
def test(name):
    return f'I am {name}.'
    

@user_has_permission            # it automatically called the my_function
def my_function(panel):
    return f'password of {panel} is 1234'               

print(my_function('sports'))
print(my_function.__name__)
print(test('Suraj'))