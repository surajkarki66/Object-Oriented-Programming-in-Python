# Inheritance

class Student:
	def __init__(self,name,school):
		self.name = name
		self.school = school
		self.marks = []


	def average(self):
		return sum(self.marks) / len(self.marks)



class WorkingStudent(Student):

	def __init__(self,name,school,salary):

		super().__init__(name,school)

		self.salary = salary



    


s = WorkingStudent('Suraj','NEC',50000)

print(s.name)
print(s.school)
print(s.salary)

s.marks.append(100)
s.marks.append(100)
s.marks.append(100)

print(s.average())
#print(s.weekly_salary())
print(s.weekly_salary)