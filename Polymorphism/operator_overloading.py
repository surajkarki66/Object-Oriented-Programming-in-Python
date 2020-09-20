# Operator overloading
a = 5
b = 6

print(a+b)

# The above print and below print is same.
print(int.__add__(a, b))

a = "Hello"
b = "World"

print(a+b)

print(str.__add__(a, b))


d = 9
print(d.__str__())


# same methods(eg: __add__) having different type argument(operands).

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        """
        This is operator
        overloading
        """
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(10, 20)
s2 = Student(30, 40)

# sum (object)
s3 = s1 + s2  # Student.__add__(s1, s2)
print(s3.m1)
print(s3.m2)

# diff(object)
s4 = s1 - s2  # Student.__sub__(s1, s2)
print(s4.m1)
print(s4.m2)


# compare
print(s1 > s2)

print(s1)
