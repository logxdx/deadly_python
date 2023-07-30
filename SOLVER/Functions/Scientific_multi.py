import math,os

def scientific_calculator():
	def menu():
		print()
		print("=== Scientific Calculator ===")
		print("Enter 's' for sine")
		print("Enter 'c' for cosine")
		print("Enter 't' for tangent")
		print("Enter 'l' for logarithm")
		print("Enter 'exp' for exponential function")
		print("Enter 'p' for power function")
		print("Enter 'r' for nth root")
		print("Enter 'a' for absolute value")
		print("Enter 'f' for factorial")
		print("Enter 'pi' for mathematical constant pi")
		print("Enter 'e' for mathematical constant e")
		print("Enter 'custom' for custom expression")
		print("Enter 'q' to quit")

	menu()
	
	while True:
		print()
		operation = input("Enter operation (m for menu): ")
		result="Enter a valid operation!!"

		if operation == 'q':
			break
		
		if operation == 'm':
			menu()
			result="Showing Menu"

		if operation in ['s', 'c', 't', 'exp', 'a', 'f']:
			number = input("Enter a number: ").replace('pi', str(math.pi)).replace('e',str(math.e)).replace('^','**')
			number = eval(number)
			result = number

		elif operation in ['p', 'r', 'l']:
			number = input("Enter the base: ").replace('pi', str(math.pi)).replace('e',str(math.e)).replace('^','**')
			number = eval(number)
			result = number

		elif operation in ['pi','e']:
			number=operation.replace('pi', str(math.pi)).replace('e',str(math.e))
			number = eval(number)
			result = number
			

		if operation == 's':
			result = math.sin(number)
			print("Result:", result)

		elif operation == 'c':
			result = math.cos(number)
			print("Result:", result)

		elif operation == 't':
			result = math.tan(number)
			print("Result:", result)

		elif operation == 'l':
			num = float(input("Enter the Number: "))
			result = math.log(num,number)
			print("Result:", result)

		elif operation == 'exp':
			result = math.exp(number)
			print("Result:", result)

		elif operation == 'p':
			exponent = float(input("Enter the exponent: "))
			result = math.pow(number, exponent)
			print("Result:", result)

		elif operation == 'r':
			root = float(input("Enter the root value: "))
			result = math.pow(number, 1 / root)
			print("Result:", result)

		elif operation == 'a':
			result = abs(number)
			print("Result:", result)

		elif operation == 'f':
			result = math.factorial(number)
			print("Result:", result)
		
		elif operation =='custom':
			while True:
				print()
				expression = input("Enter custom expression (q to exit) : ").replace('pi', str(math.pi)).replace('e',str(math.e)).replace('^','**')
				
				if expression == 'q':
					break

				try:
				# Define custom functions for each mathematical operation
					def sine(x):
						return math.sin(x)

					def cosine(x):
						return math.cos(x)

					def tangent(x):
						return math.tan(x)

					def logarithm(x):
						return math.log(x,10)
					
					def nlogarithm(x):
						return math.log(x)

					def exponential(x):
						return math.exp(x)

					def power(x, y):
						return math.pow(x, y)

					def root(x, y):
						return math.pow(x, 1/y)

					def absolute_value(x):
						return abs(x)

					def factorial(x):
						return math.factorial(x)
					
					result = eval(expression, {"__builtins__": None}, {
								"sin": sine,
								"cos": cosine,
								"tan": tangent,
								"log": logarithm,
								"ln": nlogarithm,
								"exp": exponential,
								"pow": power,
								"root": root,
								"abs": absolute_value,
								"factorial": factorial
								})

				except (SyntaxError, NameError, ZeroDivisionError):
					result=("Invalid expression")
			
				except Exception as e:
					result=("Error:", e)
					continue
				print("Result:", result)
		
		else:
			print("Error: Invalid operation")

scientific_calculator()
