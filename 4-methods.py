#!/usr/bin/python3

class Classy:
	varia = 2
	def method(self, par):
		print("method", par)
		print(self.varia)

obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

# built in properties
print(obj.__dict__)
print(Classy.__name__)			# name attribute is absent from the object
print(obj.__module__)			# module stores the name of the module which contains the class
print(Classy.__bases__)			# tuple containing classes which are direct superclasses for the class
