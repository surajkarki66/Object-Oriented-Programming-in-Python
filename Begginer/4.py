# Decorator
# Inheritance


class Student:
	def __init__(self,name,school):
		self.name = name
		self.school = school
		self.marks = []


	@property         
	def average(self):
		return sum(self.marks) / len(self.marks)


s = Student("Suraj","Nec")
s.marks.append(100)

print(s.average)