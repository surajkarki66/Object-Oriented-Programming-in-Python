# There are 2 methods in the context of encapsulation
# Public methods are called by the object in outside the class and inside also.
# Private methods are only called by the self object in inside the class.


class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

    def public_method(self):
        print(self.a)
        print(self.__c)
        print("This is public method.")
        self.__private_method()

    def __private_method(self):
        print("This is a private method")


hello = Hello("World")
hello.public_method()
# hello.__private_method() this throw an error
