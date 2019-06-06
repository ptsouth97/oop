#!/usr/bin/python3

class ExampleClass:
	__counter = 0							# this is the private class variable
	def __init__(self, val = 1):
		self.__first = val					# the __ makes the variable private
		ExampleClass.__counter += 1
		if val % 2 != 0:
			self.a = 1
		else:
			self.b = 1

exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

print(exampleObject1.__dict__, exampleObject1._ExampleClass__counter)
print(exampleObject2.__dict__, exampleObject2._ExampleClass__counter)
print(exampleObject3.__dict__, exampleObject3._ExampleClass__counter)

print(ExampleClass.__dict__)				# class variables exist even when there is no object

if hasattr(exampleObject1, 'b'):			# hasattr function checks if object/class contains a property
	print(exampleObject1)
else:
	print("doesn't exist")

print(hasattr(exampleObject1, 'a'))			
print(hasattr(ExampleClass, '_ExampleClass__counter'))			# hasattr works on classes, too
