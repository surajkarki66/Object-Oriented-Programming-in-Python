class FirstThousandGenerator:
    def __init__(self):
        self.numbers = 0

    def __next__(self):
        if self.numbers < 1000:
            current = self.numbers
            self.numbers += 1

            return current

        else:
            raise StopIteration()

    
    def __iter__(self):
        return self


g = FirstThousandGenerator()

print(next(g))
print(next(g))

#for i in g:
#    print(i)
