from abc import ABCMeta,abstractmethod
import math as m

class Area(metaclass=ABCMeta):

    @abstractmethod
    def calculation(self):
        pass

class Rectangle(Area):

    def __init__(self,length,breadth):
        self.l = length
        self.b = breadth

    def calculation(self):
        a = self.l * self.b
        return a


class Triangle(Area):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def calculation(self):
        s = (self.a+self.b+self.c)/2
        a = m.sqrt(self.a*(s-self.a)*(s-self.b)*(s-self.c))
        return a
    
a = Rectangle(1,2)
print(a.calculation())
b = Triangle(1,2,3)
print(b.calculation())

