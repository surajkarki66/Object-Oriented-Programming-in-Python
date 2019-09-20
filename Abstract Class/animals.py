from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):

    def walk(self):
        print("Walking")
                                # When abstractmethod is used we did not allowed to
                                #Create the object of animal class
                                # Now animal class is used to extract functionality
                                # It force the subclass to implement the method
    
    @abstractmethod 
    def numLegs(self):
        pass
        



class Dog(Animal):
    def __init__(self,name):
        self.name = name
    
    def numLegs(self):               # we have to define the numLeg method.
        return 4



class Monkey(Animal):

    def __init__(self,name):
        self.name = name


    def numLegs(self):
        return 2


dog = Dog("Snop")
mon = Monkey("Ram")

print(dog.numLegs())
print(mon.numLegs())

lis = [Dog("Snop"),Monkey("Ram")]

for a in lis:
    print(isinstance(a,Animal))
    print(a.numLegs())