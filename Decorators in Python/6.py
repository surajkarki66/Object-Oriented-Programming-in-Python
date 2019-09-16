# to receive iterables of arguments

def add_all(*args):
    print(args)
    return sum(args)

print(add_all(1,2,3,4))

# To receive named iterables arguments

def print1(**kwargs):                  # arguments is convert dictionary automatically
    for k,v in kwargs.items():
        print(f'For {k} we have {v}')

print1(username='suraj',password='123')
