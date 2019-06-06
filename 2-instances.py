#!/usr/bin/python3

class ExampleClass:
	def __init__(self, val = 1):
		self.__first = val				# __ makes the instance variable private

	def setSecond(self, val):
		self.__second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.__third = 5				# creates a property outside the class


print(exampleObject1.__dict__)			# __dict__ contains properties and methods
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)

print(exampleObject1._ExampleClass__first)	# access the variable outside the class
