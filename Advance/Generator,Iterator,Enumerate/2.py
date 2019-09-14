"""

Generator:
- Special Function
- Remember state its in between the execution
- You run the program multiples times it remember what he did at last time
- eg:it gives required value at a timt

"""


def century():
    i = 0
    while i is not 100:
        yield i
        i+=1

g = century()

print(next(g))
print(next(g))

# We also conver the generator into list
print(list(g))
