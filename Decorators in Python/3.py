import functools

user =   {'username':'suraj','access_level':'admin'}


def user_has_permission(func):

    @functools.wraps(func)
    def secure_func(panel):                                    # Wrapping function
            
        if user.get('access_level') == 'admin':
            return func(panel)
        raise RuntimeError

 
    return secure_func


#@ user_has_permission              # it gives an error
#def test():
 #   pass
    

@user_has_permission            # it automatically called the my_function
def my_function(panel):
    return f'password of {panel} is 1234'               

print(my_function('sports'))
print(my_function.__name__)
#print(test())


'''
# my_function() is replaced by secure_func()
# One problem when we use parameter in our decorator is that we did not apply
 decorator in any other function
'''

