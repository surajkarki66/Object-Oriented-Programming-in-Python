class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  #not accesible from object

class Bike(Car):
    def __init__(self,color):
        self.c = color
        

    def derive(self):
        print("Driving")

    def software(self):
        print("Updating")
        return self.derive()

b = Bike("Red")
b.derive()
b.software()

