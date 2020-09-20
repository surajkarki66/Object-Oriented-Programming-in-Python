# Using Static method

class FixedFloat:
	def __init__(self,amount):
		self.amount = amount

	def __repr__(self):
		return f" <FixedFloat {self.amount:.2f}> "

	@classmethod
	def from_sum(cls,value1,value2):
		return cls(value1+value2)


new_sum = FixedFloat.from_sum(10.32,4.2)

print(new_sum)



class Euro(FixedFloat):
	def __init__(self,amount):
		super().__init__(amount)
		self.symbol = 'e'

	def __repr__(self):
		return f"<Euro {self.symbol}{self.amount:.2f}>"

money = Euro.from_sum(12.34,12.45)        # The ability of class method
print(money)











