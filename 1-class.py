#!/usr/bin/python3


class Stack:							# define the Stack class
	def __init__(self):					# define the constructor function
		self.__stackList = []			# class property...the '__' makes it hidden (encapsulation)

	def push(self, val):				# public method
		self.__stackList.append(val)

	def pop(self):						# public method
		val = self.__stackList[-1]
		del self.__stackList[-1]
		return val


class AddingStack(Stack):				# Second class gets all the components of its superclass
	def __init__(self):
		Stack.__init__(self)			# explicitly invoke the superclass's constructor
		self.__sum = 0					# private variable "sum"

	def getSum(self):
		return self.__sum

	def push(self, val):
		self.__sum += val
		Stack.push(self, val)			# specify the superclass name and target object (overriding)

	def pop(self):
		val = Stack.pop(self)
		self.__sum -= val
		return val



stackObject1 = Stack() 					# instantiate the object
stackObject2 = Stack()					# instantiate a second, separate object

stackObject1.push(3)
stackObject2.push(stackObject1.pop())

print(stackObject2.pop())

###############################

stackObject = AddingStack()

for i in range(5):
	stackObject.push(i)
print(stackObject.getSum())
