# Author: Karan Deo Burnwal
# Updated on: 18/05/2023_03:23
import os,time
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from numpy.linalg import inv, det, solve, eig, svd, qr

def basic_calculator():
	print()
	print("=== Basic Calculator ===")
	print("Enter '+' to add")
	print("Enter '-' to subtract")
	print("Enter '*' to multiply")
	print("Enter '/' to divide")
	print("Enter 'q' to quit")
	print()

	while True:
		operator = input("Enter operator: ")

		if operator == 'q':
			break

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

		print("Result:", result)

def scientific_calculator():
	print()
	print("=== Scientific Calculator ===")
	print("Enter 's' for sine")
	print("Enter 'c' for cosine")
	print("Enter 't' for tangent")
	print("Enter 'l' for logarithm")
	print("Enter 'e' for exponential function")
	print("Enter 'p' for power function")
	print("Enter 'r' for nth root")
	print("Enter 'a' for absolute value")
	print("Enter 'f' for factorial")
	print("Enter 'pi' for mathematical constant pi")
	print("Enter 'e' for mathematical constant e")
	print("Enter 'q' to quit")
	print()

	while True:
		print()
		operation = input("Enter operation: ")

		if operation == 'q':
			break

		operation = operation.replace('pi', str(math.pi))
		operation = operation.replace('e', str(math.e))
		operation = operation.replace('^', '**')

		if len(operation)<=2:
			if operation in ['s', 'c', 't', 'e', 'a', 'f']:
				number = input("Enter a number: ")
			elif operation in ['p', 'r', 'l']:
				number = input("Enter the base: ")
	
			if str(number) == 'pi':
				number = math.pi
			elif str(number) == 'e':
				number = math.e
			else:
				if 'pi' in str(number):
					number=number.replace('pi','math.pi')
				elif 'e' in str(number):
					number=number.replace('e','math.e')
				number = eval(number)

		if operation == 's':
			result = math.sin(number)
		elif operation == 'c':
			result = math.cos(number)
		elif operation == 't':
			result = math.tan(number)
		elif operation == 'l':
			num = float(input("Enter the Number: "))
			result = math.log(num,number)
		elif operation == 'e':
			result = math.exp(number)
		elif operation == 'p':
			exponent = float(input("Enter the exponent: "))
			result = math.pow(number, exponent)
		elif operation == 'r':
			root = float(input("Enter the root value: "))
			result = math.pow(number, 1 / root)
		elif operation == 'a':
			result = abs(number)
		elif operation == 'f':
			result = math.factorial(number)
		else:
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

				result = eval(operation, {"__builtins__": None}, {
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
				print("Invalid expression")
			except Exception as e:
				print("Error:", e)
				continue

		print("Result:", result)

def vector_calculator():
	def cross_product(vector1, vector2):
		result = np.cross(vector1, vector2)
		print("Cross Product: ", result)
	
	def vector_triple_product(vector1, vector2, vector3):
		result = np.cross(vector1, np.cross(vector2, vector3))
		print("Vector Triple Product: ", result)
	
	def scalar_triple_product(vector1, vector2, vector3):
		result = np.dot(vector1, np.cross(vector2, vector3))
		print("Scalar Triple Product: ", result)

	while True:
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

		operation = input("Enter operation: ")

		if operation == 'q':
			break

		if operation == '+':
			vector1 = input("Enter the first vector (comma-separated values): ")
			vector2 = input("Enter the second vector (comma-separated values): ")
			vector1 = np.array([float(x) for x in vector1.split(',')])
			vector2 = np.array([float(x) for x in vector2.split(',')])
			result = vector1 + vector2
			print("Result:", result)

		elif operation == '-':
			vector1 = input("Enter the first vector (comma-separated values): ")
			vector2 = input("Enter the second vector (comma-separated values): ")
			vector1 = np.array([float(x) for x in vector1.split(',')])
			vector2 = np.array([float(x) for x in vector2.split(',')])
			result = vector1 - vector2
			print("Result:", result)

		elif operation == '*':
			vector1 = input("Enter the first vector (comma-separated values): ")
			vector2 = input("Enter the second vector (comma-separated values): ")
			vector1 = np.array([float(x) for x in vector1.split(',')])
			vector2 = np.array([float(x) for x in vector2.split(',')])
			result = np.dot(vector1, vector2)
			print("Result:", result)

		elif operation == 'x':
			vector1 = input("Enter the first vector (comma-separated values): ")
			vector2 = input("Enter the second vector (comma-separated values): ")
			vector1 = np.array([float(x) for x in vector1.split(',')])
			vector2 = np.array([float(x) for x in vector2.split(',')])
			cross_product(vector1, vector2)

		elif operation == 'vtp':
			vector1 = input("Enter the first vector (comma-separated values): ")
			vector2 = input("Enter the second vector (comma-separated values): ")
			vector3 = input("Enter the third vector (comma-separated values): ")
			vector1 = np.array([float(x) for x in vector1.split(',')])
			vector2 = np.array([float(x) for x in vector2.split(',')])
			vector3 = np.array([float(x) for x in vector3.split(',')])
			vector_triple_product(vector1, vector2, vector3)

		elif operation == 'stp':
			vector1 = input("Enter the first vector (comma-separated values): ")
			vector2 = input("Enter the second vector (comma-separated values): ")
			vector3 = input("Enter the third vector (comma-separated values): ")
			vector1 = np.array([float(x) for x in vector1.split(',')])
			vector2 = np.array([float(x) for x in vector2.split(',')])
			vector3 = np.array([float(x) for x in vector3.split(',')])
			scalar_triple_product(vector1, vector2, vector3)

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

	while True:
		print("=== Graphing Calculator ===")
		print("Enter 'p' to plot a polynomial function")
		print("Enter 't' to plot a trigonometric function")
		print("Enter 'l' to plot a logarithmic function")
		print("Enter 'e' to plot an exponential function")
		print("Enter 'c' to plot a combined function")
		print("Enter 'q' to quit")

		operation = input("Enter operation: ")

		if operation == 'q':
			break

		if operation == 'p':
			degree = int(input("Enter the degree of the polynomial: "))
			coefficients = []
			for i in range(degree, -1, -1):
				coefficient = (input("Enter the coefficient of x^{}: ".format(i)))
				if 'pi' in coefficient:
					coefficient = coefficient.replace('pi', str(math.pi))
				if 'e' in coefficient:
					coefficient = coefficient.replace('e', str(math.e))
				coefficients.append(float(coefficient))

			def polynomial_function(x):
				result = 0
				for i, coefficient in enumerate(coefficients):
					result += coefficient * x**i
				return result

			start = float(input("Enter the starting x value: "))
			end = float(input("Enter the ending x value: "))
			num_points = int(input("Enter the number of points to plot: "))

			plot_function(polynomial_function, start, end, num_points)

		elif operation == 't':
			function_type = input("Enter 's' for sine, 'c' for cosine, 't' for tangent, 'cot' for cotangent, 'sec' for secant, or 'cosec' for cosecant: ")
			amplitude 	  = (input("Enter the amplitude: "))
			frequency 	  = (input("Enter the frequency: "))
			phase_shift   = (input("Enter the phase shift (in radians): "))
			vertical_shift = (input("Enter the vertical shift: "))

			rep=[function_type, amplitude, frequency, phase_shift, vertical_shift]
			for i in rep:
				if 'pi' in i:
					i = i.replace('pi', str(math.pi))
				if 'e' in i:
					i = i.replace('e', str(math.e))
				i=float(i)

			def trigonometric_function(x):
				if function_type == 's':
					amplitude = float(input("Enter the amplitude: "))
					frequency = float(input("Enter the frequency: "))
					phase_shift = float(input("Enter the phase shift (in radians): "))
					vertical_shift = float(input("Enter the vertical shift: "))
					return amplitude * np.sin(frequency * x + phase_shift) + vertical_shift
				elif function_type == 'c':
					amplitude = float(input("Enter the amplitude: "))
					frequency = float(input("Enter the frequency: "))
					phase_shift = float(input("Enter the phase shift (in radians): "))
					vertical_shift = float(input("Enter the vertical shift: "))
					return amplitude * np.cos(frequency * x + phase_shift) + vertical_shift
				elif function_type == 't':
					return amplitude * np.tan(frequency * x + phase_shift) + vertical_shift
				elif function_type == 'cot':
					return amplitude * np.divide(1, np.tan(frequency * x + phase_shift)) + vertical_shift
				elif function_type == 'sec':
					amplitude = float(input("Enter the amplitude: "))
					frequency = float(input("Enter the frequency: "))
					phase_shift = float(input("Enter the phase shift (in radians): "))
					vertical_shift = float(input("Enter the vertical shift: "))
					return amplitude * np.divide(1, np.cos(frequency * x + phase_shift)) + vertical_shift
				elif function_type == 'cosec':
					amplitude = float(input("Enter the amplitude: "))
					frequency = float(input("Enter the frequency: "))
					phase_shift = float(input("Enter the phase shift (in radians): "))
					vertical_shift = float(input("Enter the vertical shift: "))
					return amplitude * np.divide(1, np.sin(frequency * x + phase_shift)) + vertical_shift


			start = float(input("Enter the starting x value: "))
			end = float(input("Enter the ending x value: "))
			num_points = int(input("Enter the number of points to plot: "))

			plot_function(trigonometric_function, start, end, num_points)

		elif operation == 'l':
			base = float(input("Enter the base of the logarithm: "))
			coefficient = float(input("Enter the coefficient: "))

			def logarithmic_function(x):
				return coefficient * np.log(x) / np.log(base)

			start = float(input("Enter the starting x value: "))
			end = float(input("Enter the ending x value: "))
			num_points = int(input("Enter the number of points to plot: "))

			plot_function(logarithmic_function, start, end, num_points)

		elif operation == 'e':
			base = float(input("Enter the base of the exponential function: "))
			coefficient = float(input("Enter the coefficient: "))

			def exponential_function(x):
				return coefficient * base**x

			start = float(input("Enter the starting x value: "))
			end = float(input("Enter the ending x value: "))
			num_points = int(input("Enter the number of points to plot: "))

			plot_function(exponential_function, start, end, num_points)

		elif operation == 'c':
			print("Enter 'p' for polynomial, 't' for trigonometric, 'l' for logarithmic, 'e' for exponential.")
			function_type = input("Enter the type of functions to combine (separated by comma): ")
			function_types = function_type.split(',')

			functions = []
			for func_type in function_types:
				if func_type == 'p':
					degree = int(input("Enter the degree of the polynomial: "))
					coefficients = []
					for i in range(degree, -1, -1):
						coefficient = float(input("Enter the coefficient of x^{}: ".format(i)))
						coefficients.append(coefficient)

					def polynomial_function(x):
						result = 0
						for i, coefficient in enumerate(coefficients):
							result += coefficient * x**i
						return result

					functions.append(polynomial_function)

				elif func_type == 't':
					function_type = input("Enter 's' for sine or 'c' for cosine: ")
					amplitude = float(input("Enter the amplitude: "))
					frequency = float(input("Enter the frequency: "))
					phase_shift = float(input("Enter the phase shift (in radians): "))
					vertical_shift = float(input("Enter the vertical shift: "))

					def trigonometric_function(x):
						if function_type == 's':
							return amplitude * np.sin(frequency * x + phase_shift) + vertical_shift
						elif function_type == 'c':
							return amplitude * np.cos(frequency * x + phase_shift) + vertical_shift

					functions.append(trigonometric_function)

				elif func_type == 'l':
					base = float(input("Enter the base of the logarithm: "))
					coefficient = float(input("Enter the coefficient: "))

					def logarithmic_function(x):
						return coefficient * np.log(x) / np.log(base)

					functions.append(logarithmic_function)

				elif func_type == 'e':
					base = float(input("Enter the base of the exponential function: "))
					coefficient = float(input("Enter the coefficient: "))

					def exponential_function(x):
						return coefficient * base**x

					functions.append(exponential_function)

			def combined_function(x):
				result = 0
				for func in functions:
					result += func(x)
				return result

			start = float(input("Enter the starting x value: "))
			end = float(input("Enter the ending x value: "))
			num_points = int(input("Enter the number of points to plot: "))

			plot_function(combined_function, start, end, num_points)

		else:
			print("Invalid option. Please try again.")

def linear_algebra_calculator():
	def matrix_operations(matrix1, matrix2):
		while True:
			print()
			print("=== Linear Algebra Calculator ===")
			print("Enter 'a' for matrix addition")
			print("Enter 's' for matrix addition")
			print("Enter 'm' for matrix addition")
			print("Enter 't' for matrix addition")
			print("Enter 'i' for matrix addition")
			print("Enter 'd' for matrix addition")
			print("Enter 'e' for matrix addition")
			print("Enter 'svd' for matrix addition")
			print("Enter 'qr' for matrix addition")
			print("Enter 'q' to quit")
			print()

			matrix1 = np.array(matrix1)
			matrix2 = np.array(matrix2)

			operation = input("Enter operation: ")


			if operation == 'q':
				break

			elif operation == 'a':	
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

	while True:
		print()
		print("=== Linear Algebra Calculator ===")
		print("Enter 'm' for matrix operations")
		print("Enter 'q' to quit")
		print()

		operation = input("Enter operation: ")

		if operation == 'q':
			break

		if operation == 'm':
			matrix1 = input("Enter the first matrix (rows separated by ';', columns separated by ','): ")
			matrix2 = input("Enter the second matrix (rows separated by ';', columns separated by ','): ")
			matrix1 = [list(map(float, row.split(','))) for row in matrix1.split(';')]
			matrix2 = [list(map(float, row.split(','))) for row in matrix2.split(';')]
			matrix_operations(matrix1, matrix2)
		else:
			print("Invalid input.")

def clear_screen():
    # Clear the terminal screen
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Linux and Mac
        _ = os.system('clear')

def bouncing_ball_animation():
    ball_frames = [
        r"  ___  ",
        r" / _ \ ",
        r"| |_| |",
        r" \___/ "
    ]
    direction = 1  # Initial direction (1: down, -1: up)
    position = 0  # Initial position of the ball

    while position<51:
        clear_screen()
        print("\n".join([" " * position + frame for frame in ball_frames]))  # Print the ball at the current position

        # Update position and direction
        position += direction

        # Reverse direction if the ball reaches the top or bottom
        if position == 0 or position == 150:
            direction *= -1

        time.sleep(0.00000000000000000001)  # Pause to control the speed of the animation
    clear_screen()
    print("GOODBYE!")

def main():
	while True:
		print()
		print("=== Calculator ===")
		print("Enter 'b' for basic calculator")
		print("Enter 's' for scientific calculator")
		print("Enter 'v' for vector calculator")
		print("Enter 'g' for graphing calculator")
		print("Enter 'l' for linear algebra calculator")
		print("Enter 'q' to quit")
		print()

		option = input("Enter type of calculator : ")

		if option == 'q':
			bouncing_ball_animation()
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
			linear_algebra_calculator()
		else:
			print("Invalid Input")

if __name__ == '__main__':
	main()
