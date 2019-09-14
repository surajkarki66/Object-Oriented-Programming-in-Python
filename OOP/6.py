class FixedFloat:
	def __init__(self,amount):
		self.amount = amount

	#def __repr__(self):''
	#	return f'<FixedFloat {self.amount:.2f}>'

	def from_sum(self,value1,value2):
		return FixedFloat(value1 + value2)
	



num = FixedFloat(12.1222)
new_number = num.from_sum(1,2)    # here from_sum is an instance method it is not decorator
                                  #  here new_num is an instance

print(new_number)
#print(num)
