class Garage:
	def __init__(self):               # Dunder method
		self.cars = []


	def __len__(self):                # magic/dunder method
		return len(self.cars)


	def __getitem__(self,i):          # magic method
		return self.cars[i]


	#def __repr__(self):
	#	return f"<Garage {self.cars}>"

	#def __str__(self):
	#	return f"Garage with {len(self)} cars"


car = Garage()

car.cars.append("BMW")
car.cars.append("Buggati")

print(car.cars)

print(len(car))

print(car[0])


# After implementinf these 2 dunder method then you can do certein new things:

#for car in car:
#	print(car)

print(car)
