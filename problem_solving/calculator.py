class Calculator:
	def __init__(self, number1, number2):
		self.number1  = int(number1)
		self.number2  = int(number2)
		
	def add(self):
		return self.number1 + self.number2

	def sub(self):
		return self.number1 - self.number2

	def mult(self):
		return self.number1 * self.number2

	def div(self):
		return self.number1 / self.number2

print('\n****PYTHON CALCULATOR - with classes****\n')
number1 = input('Write the first number: ')
number2 = input('Write the second number: ')
operator = input('Write the operator: (+, -, x, /) ')
calc = Calculator(number1, number2)
if operator == '+': 
	result = calc.add()
elif operator == '-':
	result = calc.sub()
elif operator == 'x':
	result = calc.mult()
elif operator == '/':
	result = calc.div()
else:
	print('Write a valid operator.')

print('\nThe result of this operation is: ', result)
