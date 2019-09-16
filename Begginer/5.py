class Foo:
	@classmethod          # In classmethod takes class of the caller as first argument rather than self
	def hi(cls):
		print(cls.__name__)


f = Foo()

f.hi()


class Bar:
	@staticmethod
	def hi():
		print('hello i dont take any argument')



b  = Bar()

b.hi()



