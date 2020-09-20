# Polymorphism means a single thing can have many forms.
# Just like that a single object has many forms

# Example of inbuilt polymorphic functions :

# Python program to demonstrate in-built poly-
# morphic functions

# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))


# Examples of used defined polymorphic functions :
# A simple Python function to demonstrate
# Polymorphism

def add(x, y, z=0):
    return x + y + z


# Driver code
print(add(2, 3))
print(add(2, 3, 4))


class PyCharm:
    def execute(self):
        print("Take too time")
        print("Compiling")
        print("Running")


class VsCode:
    def execute(self):
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = VsCode()
#ide = PyCharm()

l = Laptop()
l.code(ide)
