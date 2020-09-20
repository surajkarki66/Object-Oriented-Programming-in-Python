# In OOPs there are two types of variables:
# 1) Instance Variable
# 2) Class Variable(static variable)

class Car:
    """
    Types of variable
    """
    # class variable
    wheels = 4

    def __init__(self):
        # instance variable

        self.mil = 10
        self.com = "BMW"

    def info(self):
        """
        Info About Cars
        """
        print("Milaze: ", self.mil)
        print("Company: ", self.com)


c1 = Car()
c2 = Car()

print(c1.mil)
print(c1.com)

c1.mil = 12

print(c1.mil)

print(c1.wheels)
print(c2.wheels)

Car.wheels = 10

print(c1.wheels)
print(c2.wheels)
