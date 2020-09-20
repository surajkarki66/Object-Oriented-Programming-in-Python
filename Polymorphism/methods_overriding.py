# In python there is no method overloading feature
class A:
    def show(self):
        print('In A Show')


class B(A):
    def show(self):
        print('In B Show')


b1 = B()

# if there was no methods inside the B class then it goes for show method of base class
# if class B has same method name as base class A then it overrides the method of A with his own show method
b1.show()
