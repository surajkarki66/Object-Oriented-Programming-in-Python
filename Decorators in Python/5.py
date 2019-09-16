def add_all(a1,a2,a3,a4):
    return a1+a2+a3+a4

vals = (1,3,5,7)

print(add_all(*vals))

# To pass named arguments
vals = {'a1':1,'a2':3,'a3':5,'a4':7}

print(add_all(**vals))