# All objects that have dunder __next__() method are callled iterators
# Iterables is an object that have iter method
# Iterables helps to iterate over generator
# Iterator is used to get next value
# Iterables is used to go over all the values of the iterator


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1

        else:
            raise StopIteration()

        return current

    

class FirstHundredIterables:
    def __iter__(self):
        return FirstHundredGenerator()


print(sum(FirstHundredIterables()))

for i in FirstHundredIterables():
    print(i)

