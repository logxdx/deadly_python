# Author: Karan Deo Burnwal
# Updated on: 19/05/2023_00:05
# Improved graphing calculator

import os,time
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from numpy.linalg import inv, det, solve, eig, svd, qr

def basic_calculator():
	def menu():
		print()
		print("=== Basic Calculator ===")
		print("Enter '+' to add")
		print("Enter '-' to subtract")
		print("Enter '*' to multiply")
		print("Enter '/' to divide")
		print("Enter 'q' to quit")
		print()

	menu()

	while True:
		print()
		operator = input("Enter operator (m for menu) : ")

		if operator == 'q':
			break
		
		if operator in '+-*/':
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))

		if operator == '+':
			result = num1 + num2
		elif operator == '-':
			result = num1 - num2
		elif operator == '*':
			result = num1 * num2
		elif operator == '/':
			if num2 != 0:
				result = num1 / num2
			else:
				print("Error: Division by zero")
				continue
		elif operator == 'm':
			menu()
			result='Showing Menu\n'
		else:
			result=("Error: Invalid operator")

		print("Result:", result)

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

def vector_calculator():
	def vector_operations(vector1,vector2,operation,vector3=None):
		
		if operation == '+':
			result = vector1 + vector2
			print("Vector Addition :")
			print(result)

		elif operation == '-':
			result = vector1 - vector2
			print("Vector Subtraction :")
			print(result)

		elif operation == '*':
			result = np.dot(vector1, vector2)
			print("Dot prodcut :")
			print(result)

		elif operation == 'x':			
			result = np.cross(vector1, vector2)
			print("Cross Product: ")
			print(result)

		elif operation == 'stp':
			result = np.dot(vector1, np.cross(vector2, vector3))
			print("Scalar Triple Product: ")
			print(result)

		elif operation == 'vtp':
			result = np.cross(vector1, np.cross(vector2, vector3))
			print("Vector Triple Product: ")
			print(result)

	def menu():
		print()
		print("=== Vector Calculator ===")
		print("Enter '+' to add vectors")
		print("Enter '-' to subtract vectors")
		print("Enter '*' to dot product")
		print("Enter 'x' to cross product")
		print("Enter 'vtp' to calculate vector triple product")
		print("Enter 'stp' to calculate scalar triple product")
		print("Enter 'q' to quit")
		print()

	menu()

	while True:
		print()
		operation = input("Enter operation (m for menu): ")

		if operation == 'q':
			break

		if operation in '+-*x':
			vector1 = input("Enter the first vector (comma-separated values): ")
			vector2 = input("Enter the second vector (comma-separated values): ")
			vector1 = np.array([float(x) for x in vector1.split(',')])
			vector2 = np.array([float(x) for x in vector2.split(',')])
			vector_operations(vector1, vector2, operation)

		elif operation in 'stpvtp':
			vector1 = input("Enter the first vector (comma-separated values): ")
			vector2 = input("Enter the second vector (comma-separated values): ")
			vector3 = input("Enter the third vector (comma-separated values): ")
			vector1 = np.array([float(x) for x in vector1.split(',')])
			vector2 = np.array([float(x) for x in vector2.split(',')])
			vector3 = np.array([float(x) for x in vector3.split(',')])
			vector_operations(vector1, vector2, operation, vector3)

		elif operation == 'm':
			menu()

		else:
			print("Error: Invalid operation.")

def graphing_calculator():
	def plot_function(func, start, end, num_points):
		x = np.linspace(start, end, num_points)
		y = func(x)

		plt.plot(x, y, label='Function')

		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Graph of the Function')
		plt.grid(True)
		plt.legend()
		plt.show()

	def polynomial():
		degree = int(input("Enter the degree of the polynomial: "))
		coefficients = []
		for i in range(degree, -1, -1):
			coefficient = eval(input("Enter the coefficient of x^{}: ".format(i)).replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
			coefficients.append(float(coefficient))
		
		def polynomial_function(x):
			result = 0
			for i, coefficient in enumerate(coefficients[::-1]):
				result += coefficient * x**i
			return result

		start = float(input("Enter the starting x value: "))
		end = float(input("Enter the ending x value: "))
		num_points = int(input("Enter the number of points to plot: "))

		plot_function(polynomial_function, start, end, num_points)

	def trigonometry():
		function_type = input("Enter 's' for sine, 'c' for cosine, 't' for tangent, 'cot' for cotangent, 'sec' for secant, or 'cosec' for cosecant: ")
		if function_type in 'scseccosec':
			amplitude 	  = eval(input("Enter the amplitude: ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		frequency 	  = eval(input("Enter the frequency: ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		phase_shift   = eval(input("Enter the phase shift (in radians): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		vertical_shift = eval(input("Enter the vertical shift: ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))

		def trigonometric_function(x):
			if function_type == 's':
				return amplitude * np.sin(frequency * x + phase_shift) + vertical_shift
			elif function_type == 'c':
				return amplitude * np.cos(frequency * x + phase_shift) + vertical_shift
			elif function_type == 't':
				return amplitude * np.tan(frequency * x + phase_shift) + vertical_shift
			elif function_type == 'cot':
				return amplitude * np.divide(1, np.tan(frequency * x + phase_shift)) + vertical_shift
			elif function_type == 'sec':
				return amplitude * np.divide(1, np.cos(frequency * x + phase_shift)) + vertical_shift
			elif function_type == 'cosec':
				return amplitude * np.divide(1, np.sin(frequency * x + phase_shift)) + vertical_shift


		start = float(input("Enter the starting x value: "))
		end = float(input("Enter the ending x value: "))
		num_points = int(input("Enter the number of points to plot: "))

		plot_function(trigonometric_function, start, end, num_points)

	def logarithm():
		print("||Example: a*(log(b*x))/(log(base))||\n||Base is greater than 0 and not equal to 1||")
		base = eval(input("Enter the base of the logarithm (base): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		coefficient = eval(input("Enter the coefficient (a): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		coeff = eval(input("Enter the multiplier coefficient (b): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		
		def logarithmic_function(x):
			return float(coefficient) * np.log(coeff*x) / np.log(base)

		start = float(input("Enter the starting x value: "))
		end = float(input("Enter the ending x value: "))
		num_points = int(input("Enter the number of points to plot: "))

		plot_function(logarithmic_function, start, end, num_points)

	def exponential():
		print("||Example: a*((base)^(b*x))||\n||Base is greater than 0 and not equal to 1||")
		base = eval(input("Enter the base of the exponential function (base): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		coefficient = eval(input("Enter the coefficient (a): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		coeff = eval(input("Enter the multiplier coefficient (b): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))

		def exponential_function(x):
			return coefficient * base**(b*x)

		start = float(input("Enter the starting x value: "))
		end = float(input("Enter the ending x value: "))
		num_points = int(input("Enter the number of points to plot: "))

		plot_function(exponential_function, start, end, num_points)

	def menu():
		print("=== Graphing Calculator ===")
		print("Enter 'p' to plot a polynomial function")
		print("Enter 't' to plot a trigonometric function")
		print("Enter 'l' to plot a logarithmic function")
		print("Enter 'e' to plot an exponential function")
		print("Enter 'q' to quit")

	menu()

	while True:
		print()
		operation = input("Enter operation (m for menu) : ")

		if operation == 'q':
			break

		if operation == 'p':
			polynomial()

		elif operation == 't':
			trigonometry()

		elif operation == 'l':
			logarithm()

		elif operation == 'e':
			exponential()

		elif operation == 'm':
			menu()

		else:
			print("Error: Invalid operation")

def matrix_calculator():
	def matrix_operations(matrix1, operation, matrix2=None):
			matrix1 = np.array(matrix1)
			if operation in 'asmtd':
				matrix2 = np.array(matrix2)

			if operation == 'a':	
				print("Matrix Addition:")
				print(matrix1 + matrix2)
			elif operation == 's':	
				print("Matrix Subtraction:")
				print(matrix1 - matrix2)
			elif operation == 'm':	
				print("Matrix Multiplication:")
				print(matrix1 @ matrix2)
			elif operation == 't':	
				print("Matrix Transpose:")
				print(matrix1.T)
				print(matrix2.T)
			elif operation == 'i':	
				print("Matrix Inverse:")
				try:
					inv_matrix = inv(matrix1)
					print(inv_matrix)
				except np.linalg.LinAlgError:
					print("Matrix is not invertible.")
			elif operation == 'd':	
				print("Matrix Determinant:")
				print(det(matrix1))
				print(det(matrix2))
			elif operation == 'e':	
				print("Matrix Eigenvalues and Eigenvectors:")
				eig_vals, eig_vecs = eig(matrix1)
				for i in range(len(eig_vals)):
					print("Eigenvalue:", eig_vals[i])
					print("Eigenvector:", eig_vecs[:, i])
			elif operation == 'svd':	
				print("Matrix Singular Value Decomposition (SVD):")
				U, S, V = svd(matrix1)
				print("U:", U)
				print("S:", S)
				print("V:", V)
			elif operation == 'qr':	
				print("Matrix QR Decomposition:")
				Q, R = qr(matrix1)
				print("Q:", Q)
				print("R:", R)

	def menu():
			print()
			print("=== Linear Algebra Calculator ===")
			print("Enter 'a' for matrix addition")
			print("Enter 's' for matrix subtraction")
			print("Enter 'm' for matrix multiplication")
			print("Enter 't' for matrix transpose")
			print("Enter 'i' for matrix inverse")
			print("Enter 'd' for matrix determinant")
			print("Enter 'e' for matrix eigenvalues and eigenvectors")
			print("Enter 'svd' for matrix Singular Value Decomposition")
			print("Enter 'qr' for matrix QR Decomposition")
			print("Enter 'q' to quit")
			print()

	menu()

	while True:
		print()
		operation = input("Enter operation (m for menu) : ")

		if operation == 'q':
			break

		elif operation in 'asmtd':
			matrix1 = input("Enter the first matrix (rows separated by ';', columns separated by ','): ")
			matrix2 = input("Enter the second matrix (rows separated by ';', columns separated by ','): ")
			matrix1 = [list(map(float, row.split(','))) for row in matrix1.split(';')]
			matrix2 = [list(map(float, row.split(','))) for row in matrix2.split(';')]
			matrix_operations(matrix1, operation, matrix2)
		elif operation in 'iesvdqr':
			matrix1 = input("Enter the matrix (rows separated by ';', columns separated by ','): ")
			matrix1 = [list(map(float, row.split(','))) for row in matrix1.split(';')]
			matrix_operations(matrix1, operation)
		elif operation in 'm':
			menu()
		else:
			print("Error: Invalid operation")

def clear_screen():
	# Clear the terminal screen
	if os.name == 'nt':  # For Windows
		_ = os.system('cls')
	else:  # For Linux and Mac
		_ = os.system('clear')

def main():
	while True:
		print()
		print("=== Calculator ===")
		print("Enter 'b' for Basic Calculator")
		print("Enter 's' for Scientific Calculator")
		print("Enter 'v' for Vector Calculator")
		print("Enter 'g' for Graphing Calculator")
		print("Enter 'l' for Matrix Operation")
		print("Enter 'cls' to Clear Screen")
		print("Enter 'q' to Quit")
		print()

		option = input("Enter type of calculator : ")

		if option == 'q':
			clear_screen()
			break

		if option == 'b':
			basic_calculator()
		elif option == 's':
			scientific_calculator()
		elif option == 'v':
			vector_calculator()
		elif option == 'g':
			graphing_calculator()
		elif option == 'l':
			matrix_calculator()
		elif option == 'cls':
			clear_screen()
		else:
			print("Error: Invalid Input")

if __name__ == '__main__':
	clear_screen()
	main()
