# Using Static method

class FixedFloat:
	def __init__(self,amount):
		self.amount = amount

	@staticmethod
	def from_sum(value1,value2):
		return FixedFloat(value1+value2)


new_sum = FixedFloat.from_sum(10.32,4.2)

print(new_sum)



class Euro(FixedFloat):
	def __init__(amount):
		super().__init__(amount)
		self.symbol = 'e'

money = Euro.from_sum(12.34,12.45)
print(money)
