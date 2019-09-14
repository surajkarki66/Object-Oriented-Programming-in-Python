# Generator using class 
# objects remains and remenber self.number

class FirstThousandsGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 1000:
            current = self.number
            self.number += 1

        else:
            raise StopIteration()

        return current

g = FirstThousandsGenerator()

print(next(g))
print(next(g))
print(next(g))