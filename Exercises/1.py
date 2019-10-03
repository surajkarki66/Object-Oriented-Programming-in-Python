import math as m

class Point:

    def __init__(self, x, y):
        self.move(x, y)


    def move(self, x, y):
        self.x = x
        self.y = y


    def reset(self):
        self.move(0, 0)


    def distance(self,other_point):
        return m.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )


point1 = Point(1,2)
point2 = Point(3,4)

point1.reset()
print(point2.distance(point1))