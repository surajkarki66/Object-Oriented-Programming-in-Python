class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        self.lap.show()
        print(self.name, self.rollno)

    class Laptop:
        """
        This is inner class
        """

        def __init__(self):
            self.brand = 'Dell'
            self.cpu = 'i7'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Suraj", 339)
# s1.show()

print(s1.name)
print(s1.rollno)
# print(s1.lap.brand)
# print(s1.lap.cpu)
# print(s1.lap.ram)

s2 = Student("Binish", 324)
s2.show()
