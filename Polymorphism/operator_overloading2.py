class Mass:
    def __init__(self, m):
        self.m = m

    def __add__(self, other):
        m = self.m + other.m
        m3 = Mass(m)
        return m3

    def __sub__(self, other):
        m = self.m - other.m
        m4 = Mass(m)
        return m4

    def __gt__(self, other):
        r1 = self.m
        r2 = other.m
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{}'.format(self.m)


m1 = Mass(10)
m2 = Mass(20)

m3 = m1 + m2  # Mass.__add__(m1, m2)
print(m3.m)

m4 = m1 - m2  # Mass.__sub__(m1, m2)
print(m4.m)

print(m2 > m1)  # Mass.__gt__(m1, m2)

print(m1)  # Mass.__str__(m1)
