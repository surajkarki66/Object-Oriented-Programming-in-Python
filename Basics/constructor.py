class Computer():
    # Constructor in python is the special method that we are overriding.
    def __init__(self, cpu: str, ram: int):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ", self.cpu, self.ram)


comp1 = Computer('i5', 16)
comp2 = Computer('Ryzen3', 8)

comp1.config()
comp2.config()
