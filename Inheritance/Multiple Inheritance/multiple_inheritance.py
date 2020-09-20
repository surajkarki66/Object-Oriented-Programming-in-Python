class A:
    """
    Parent class
    """

    def feature1(self):
        print("This is a feature 1")

    def feature2(self):
        print("This is a feature 2")


class B:
    """
    Parent class
    """

    def feature3(self):
        print("This is a feature 3")

    def feature4(self):
        print("This is a feature 4")


class C(A, B):
    """
    Child class
    """

    def feature5(self):
        print("This is a feature 5")

    def feature6(self):
        print("This is a feature 6")


c1 = C()

c1.feature1()
c1.feature2()

c1.feature3()
c1.feature4()
