class A:
    """
    Base class
    """

    def __init__(self):
        print("Init in A")

    def feature1(self):
        print("This is a feature 1")

    def feature2(self):
        print("This is a feature 2")


class B(A):
    """
    Child class
    """

    def __init__(self):
        super().__init__()  # calling the __init__ method of base class.
        print("Init in B")

    def feature3(self):
        print("This is a feature 3")

    def feature4(self):
        print("This is a feature 4")


b1 = B()
b1.feature1()
b1.feature2()
