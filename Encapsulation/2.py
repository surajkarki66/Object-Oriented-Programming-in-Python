class Car:
	
	__speed = 0
	__name = ""

	def __init__(self):
		
		self.__speed = 360
		self.__name = "Lamborghini"

	def detail(self):
		print("The name of the car is ",self.__name)

		print("The speed of the car is",self.__speed)




lambo = Car()
lambo.detail()

lambo.__speed = 23
lambo.detail()

# To change the private variables we have to use setter

class Buggati(Car):
	
	def __init__(self):
		self.speed = __speed  # Not accessed private data

	def detail(self):
		print(self.speed)
		print(self.__speed)

b = Buggati()
b.detail()
