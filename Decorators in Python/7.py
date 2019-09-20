import functools

def calc(func):
     
    @functools.wraps(func)
    def wrap(*args,**kwargs):
        input1 = input("Enter y for go:")
        if input1 == 'y':
            return func(*args,**kwargs)

    return wrap


@calc
def even(num):
    if num % 2 == 0:
        return f'{num} is even.'
    else:
        return f'{num} is odd.'

@calc      
def fibonacci(n):

    i = 3
    a = 0
    b = 1
    print(a)
    while(i<n):
        c = a + b
        a = b
        b = c
        i+=1
        
        print(c)


print(even(8))
fibonacci(12)



    

    