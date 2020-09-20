# There three types of methods.
# 1) Instance methods
# 2) Class methods
# 3) Static methods


class Students:
    """
    Students class
    """
    # class variable
    school = 'Coursera'

    def __init__(self, m1, m2, m3):
        # instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        """
        Instance
        Methods
        """
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        """
        Class 
        Method: it access only class variable
        """
        return cls.school

    @staticmethod
    def info():
        """
        Static
        method: it has nothing to do with instance var and class var
        """
        return("This is a students class")


s1 = Students(12, 13, 45)
s2 = Students(14, 34, 32)

# calling instance method
print(s1.avg())
# calling class method
print(Students.getSchool())
# calling static method
print(Students.info())
