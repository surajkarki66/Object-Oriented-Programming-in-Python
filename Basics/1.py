class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grade = new_grade

    def average(self):

        return sum(self.grade) / len(self.grade)


student_one = Student('Suraj Karki', [100, 100, 100])

name = student_one.name

avg = student_one.average()

print(name)

print(avg)

# print(student_one.__class__)


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year


holly = Movie("Aladdin", 2019)

# print(holly)
print(holly.name)
print(holly.year)


lists = [1, 2, 3, 4, 5]
tuples = tuple(lists)
print(lists.__class__)
print(tuples.__class__)
