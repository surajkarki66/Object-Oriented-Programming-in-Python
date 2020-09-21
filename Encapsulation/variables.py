# There are 2 variables in the context of encapsulation
# Public variables are accessed by the object in outside the class and inside also.
# Private variables are only accessed by the self object in inside the class.

# In python private variables is denoted by _variablename and for complete private __variablename.

class Car:
    # private class variable
    __class_variable = "Car"

    def __init__(self, speed, color):
        # All below instance variables are private variables
        self.__speed = speed
        self.__color = color

    def get_car_info(self):
        """
        Fetching private attributes inside the class.
        """
        return '{} {}'.format(self.__speed, self.__color)

    def update_car_info(self, speed, color):
        """
        Updating private attributes inside the class
        """
        self.__speed = speed
        self.__color = color

    @classmethod
    def get_class_variable(cls):
        return cls.__class_variable


ford = Car(150, "red")
# ford.__color = "black" we cannot change the private attribute outside the class.
# print(ford.__speed) this gives us an error.Because we cannot access private var outside class
# print(Car.__class_variable) you cannot access private class variable outside the class

# Getting the private class variable
print(Car.get_class_variable())

# Getting the private attributes
print(ford.get_car_info())

# Updating the private attributes
ford.update_car_info(200, "Pink")

# Getting the private attributes
print(ford.get_car_info())


# Another example

class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def area(self):
        return self.__width * self.__height


r = Rectangle(10, 20)
# print(r.__height)

print(r.get_height())
print(r.get_width())

print(r.area())

r.set_height(20)
r.set_width(30)

print(r.get_height())
print(r.get_width())

print(r.area())
