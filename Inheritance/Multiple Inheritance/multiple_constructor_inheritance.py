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


class B:
    """
    Base class
    """

    def __init__(self):
        print("Init in B")

    def feature3(self):
        print("This is a feature 3")

    def feature4(self):
        print("This is a feature 4")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("Init in C")


c1 = C()
c1.feature1()
c1.feature2()

c1.feature3()
c1.feature4()
