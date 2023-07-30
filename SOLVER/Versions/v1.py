# Python code that implements a calculator, 
# capable of performing basic arithmetic, scientific, vector, and graphing calculations
# Author: Karan Deo Burnwal
# Created on : 16/05/2023_19:26
'''
You can run the code and choose the desired calculator option (basic, scientific, vector, or graphing) to perform the corresponding calculations.
'''




import math
import matplotlib.pyplot as plt
import numpy as np


def basic_calculator():
	while True:
		print("=== Basic Calculator ===")
		print("Enter '+' to add")
		print("Enter '-' to subtract")
		print("Enter '*' to multiply")
		print("Enter '/' to divide")
		print("Enter 'q' to quit")

		operator = input("Enter operator: ")

		if operator == 'q':
			break

		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

		if operator == '+':
			result = num1 + num2
			print("Result: ", result)
		elif operator == '-':
			result = num1 - num2
			print("Result: ", result)
		elif operator == '*':
			result = num1 * num2
			print("Result: ", result)
		elif operator == '/':
			if num2 != 0:
				result = num1 / num2
				print("Result: ", result)
			else:
				print("Error: Division by zero!")

def scientific_calculator():
	while True:
		print("=== Scientific Calculator ===")
		print("Enter 's' for sine")
		print("Enter 'c' for cosine")
		print("Enter 't' for tangent")
		print("Enter 'l' for logarithm")
		print("Enter 'q' to quit")

		operation = input("Enter operation: ")

		if operation == 'q':
			break

		num = float(input("Enter a number: "))

		if operation == 's':
			result = math.sin(num)
			print("Result: ", result)
		elif operation == 'c':
			result = math.cos(num)
			print("Result: ", result)
		elif operation == 't':
			result = math.tan(num)
			print("Result: ", result)
		elif operation == 'l':
			result = math.log10(num)
			print("Result: ", result)

def vector_calculator():
	while True:
		print("=== Vector Calculator ===")
		print("Enter '+' to add vectors")
		print("Enter '-' to subtract vectors")
		print("Enter '*' to dot product")
		print("Enter 'q' to quit")

		operation = input("Enter operation: ")

		if operation == 'q':
			break

		vector1 = input("Enter the first vector (comma-separated values): ")
		vector2 = input("Enter the second vector (comma-separated values): ")

		vector1 = [float(x) for x in vector1.split(',')]
		vector2 = [float(x) for x in vector2.split(',')]

		if operation == '+':
			result = [x + y for x, y in zip(vector1, vector2)]
			print("Result: ", result)
		elif operation == '-':
			result = [x - y for x, y in zip(vector1, vector2)]
			print("Result: ", result)
		elif operation == '*':
			result = sum([x * y for x, y in zip(vector1, vector2)])
			print("Result: ", result)

def graphing_calculator():
	x = np.linspace(-20, 20, 1000)
	while True:
		print("=== Graphing Calculator ===")
		print("Enter 'p' to plot a function")
		print("Enter 'q' to quit")

		operation = input("Enter operation: ")

		if operation == 'q':
			break

		if operation == 'p':
			function = input("Enter a function: ")
			try:
				y = eval(function)
				plt.plot(x, y)
				plt.xlabel('x')
				plt.ylabel('y')
				plt.title('Graph of ' + function)
				plt.grid(True)
				plt.show()
			except:
				print("Invalid function!")

def main():
	while True:
		print()
		print("=== Calculator ===")
		print("Enter 'b' for basic calculator")
		print("Enter 's' for scientific calculator")
		print("Enter 'v' for vector calculator")
		print("Enter 'g' for graphing calculator")
		print("Enter 'q' to quit")
		print()
		option = input("Enter option: ")

		if option == 'q':
			break

		if option == 'b':
			basic_calculator()
		elif option == 's':
			scientific_calculator()
		elif option == 'v':
			vector_calculator()
		elif option == 'g':
			graphing_calculator()

if __name__ == '__main__':
	main()
