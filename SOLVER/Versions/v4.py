# Author: Karan Deo Burnwal
# Updated on: 21/05/2023_19:08
# Improved optimised Code

import os,time
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from numpy.linalg import inv, det, solve, eig, svd, qr

def calculator(option):
	def mathematical_parser(s):
		s=s.replace('d', '*(pi)/180')
		s=s.replace('pi', 'math.pi').replace('e','math.e').replace('^','**')
		s=s.replace('sqrt','math.sqrt').replace('pow', 'math.pow').replace('abs', 'math.abs')
		s=s.replace('sin','math.sin').replace('amath.sin','math.asin')
		s=s.replace('cos','math.cos').replace('amath.cos','math.cos')
		s=s.replace('tan','math.tan').replace('amath.tan','math.atan')
		s=s.replace('log', 'math.log')
		s=s.replace('C', 'math.comb').replace('P','math.perm')
		
		return s

	def parser_value(s):
		return eval(mathematical_parser(s))

	def scientific_calculator():
		clear_screen()

		print()
		print("=== Scientific Calculator ===")
		print("Enter 'q' to quit")
		
		while True:
			print()
			expression = input("Enter expression : ")

			if expression == 'q':
				break
			
			elif 'ans' in expression:
				result=parser_value(expression.replace('ans', 'result'))
			
			else:
				try:
					result=eval(mathematical_parser(expression))
				
				except (SyntaxError, NameError, ZeroDivisionError):
					result=("Invalid expression")
				
				except Exception as e:
					result=("Error:", e)
					continue
			
			print(result)

	def vector_calculator():
		clear_screen()

		def vector_operations(vector1,vector2,operation=None,vector3=None):
			if operation=="1":
					
					print()
					
					result = vector1 + vector2
					print("Vector Addition :")
					print(result)

					print()

					result = vector1 - vector2
					print("Vector Subtraction :")
					print(result)

					print()

					result = np.dot(vector1, vector2)
					print("Dot prodcut :")
					print(result)

					print()

					result = np.cross(vector1, vector2)
					print("Cross Product: ")
					print(result)

			elif operation == '2':
				v={'1':vector1,'2':vector2,'3':vector3}

				print()
				
				result = vector1 + vector2 + vector3
				print("Vector Addition :")
				print(result)

				print()
				
				dot=input("Select vectors for dot product (Enter 1,2 or 3 with a space): ").split()
				result = np.dot(v[dot[0]], v[dot[1]])
				print("Dot prodcut :")
				print(result)

				print()
				
				cross=input("Select vectors for cross product (Enter 1,2 or 3 with a space): ").split()
				result = np.cross(v[cross[0]], v[cross[1]])
				print("Cross Product: ")
				print(result)

				print()

				result = np.dot(vector1, np.cross(vector2, vector3))
				print("Scalar Triple Product: ")
				print(result)

				print()

				result = np.cross(vector1, np.cross(vector2, vector3))
				print("Vector Triple Product: ")
				print(result)

		def menu():
			print()
			print("=== Vector Calculator ===")
			print("Enter '1' for vector addition, subtraction, dot product, cross product")
			print("Enter '2' to calculate vector triple product and scalar triple product and all the above")
			print("Enter 'q' to quit")
			print()

		menu()

		while True:
			print()
			operation = input("Enter operation (m for menu): ")

			if operation == 'q':
				break

			if operation in '1':
				vector1 = input("Enter the first vector (comma-separated values): ")
				vector2 = input("Enter the second vector (comma-separated values): ")
				vector1 = np.array([parser_value(x) for x in vector1.split(',')])
				vector2 = np.array([parser_value(x) for x in vector2.split(',')])
				vector_operations(vector1, vector2, operation)

			elif operation in '2':
				vector1 = input("Enter the first vector (comma-separated values): ")
				vector2 = input("Enter the second vector (comma-separated values): ")
				vector3 = input("Enter the third vector (comma-separated values): ")
				vector1 = np.array([parser_value(x) for x in vector1.split(',')])
				vector2 = np.array([parser_value(x) for x in vector2.split(',')])
				vector3 = np.array([parser_value(x) for x in vector3.split(',')])
				vector_operations(vector1, vector2, operation, vector3)

			elif operation == 'm':
				menu()

			else:
				print("Error: Invalid operation.")

	def graphing_calculator():
		clear_screen()

		def plot_function(func, start, end, num_points,name):
			
			x = np.linspace(start, end, num_points)
			y = func(x)

			plt.plot(x, y, label='Function')

			plt.xlabel('x')
			plt.ylabel('y')
			plt.title(name+' Function')
			plt.grid(True)
			plt.legend()
			plt.show()

		def polynomial():
			
			degree = int(input("Enter the degree of the polynomial: "))
			coefficients = []
			
			for i in range(degree, -1, -1):
				coefficient = parser_value(input("Enter the coefficient of x^{}: ".format(i)))
				coefficients.append(coefficient)
			
			def polynomial_function(x):
				result = 0
				for i, coefficient in enumerate(coefficients[::-1]):
					result += coefficient * x**i
				return result

			start = parser_value(input("Enter the starting x value: "))
			end = parser_value(input("Enter the ending x value: "))
			num_points = int(input("Enter the number of points to plot: "))

			plot_function(polynomial_function, start, end, num_points, 'Polynomial')

		def trigonometry():
			
			function_type  = input("Enter 's' for sine, 'c' for cosine, 't' for tangent, 'cot' for cotangent, 'sec' for secant, or 'cosec' for cosecant: ")
			amplitude 	   = parser_value(input("Enter the amplitude: "))
			frequency 	   = parser_value(input("Enter the frequency: "))
			phase_shift    = parser_value(input("Enter the phase shift (in radians): "))
			vertical_shift = parser_value(input("Enter the vertical shift: "))

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

			start = parser_value(input("Enter the starting x value: "))
			end = parser_value(input("Enter the ending x value: "))
			num_points = int(input("Enter the number of points to plot: "))

			plot_function(trigonometric_function, start, end, num_points, "Trigonometric")

		def logarithm():
			
			print("Example:") 
			print("||a*(log(b*x))/(log(base))||")
			print("||Base is greater than 0 and not equal to 1||")

			base = parser_value(input("Enter the base of the logarithm (base): "))
			coefficient = parser_value(input("Enter the coefficient (a): "))
			coeff = parser_value(input("Enter the multiplier coefficient (b): "))
			
			def logarithmic_function(x):
				return coefficient * np.log(coeff*x) / np.log(base)
			
			start = parser_value(input("Enter the starting x value: "))
			end = parser_value(input("Enter the ending x value: "))
			num_points = int(input("Enter the number of points to plot: "))

			plot_function(logarithmic_function, start, end, num_points, "Logarithmic")

		def exponential():
			
			print("Example:")
			print("||a*((base)^(b*x))||")
			print("||Base is greater than 0 and not equal to 1||")
			
			base = parser_value(input("Enter the base of the exponential function (base): "))
			coefficient = parser_value(input("Enter the coefficient (a): "))
			coeff = parser_value(input("Enter the multiplier coefficient (b): "))

			def exponential_function(x):
				return coefficient * base**(coeff*x)

			start = parser_value(input("Enter the starting x value: "))
			end = parser_value(input("Enter the ending x value: "))
			num_points = int(input("Enter the number of points to plot: "))

			plot_function(exponential_function, start, end, num_points, "Exponential")

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
		clear_screen()

		def matrix_operations(matrix1, operation=None, matrix2=None):

			matrix1 = np.array(matrix1)
			
			if operation in '1':
				
				matrix2 = np.array(matrix2)

				print()

				print("Matrix Addition:")
				print(matrix1 + matrix2)

				print()

				print("Matrix Subtraction:")
				print(matrix1 - matrix2)

				print()

				print("Matrix Multiplication:")
				print(matrix1 @ matrix2)

				print()

				print("Matrix Transpose:")
				print("Matrix1 :", matrix1.T)
				print("Matrix2 :", matrix2.T)

				print()

				print("Matrix Inverse:")
				try:
					inv_matrix1 = inv(matrix1)
					print("Matrix1 :",inv_matrix)
				except np.linalg.LinAlgError:
					print("Matrix1 is not invertible.")
				try:
					inv_matrix2 = inv(matrix2)
					print("Matrix2 :",inv_matrix2)
				except np.linalg.LinAlgError:
					print("Matrix2 is not invertible.")
				
				print()

				print("Matrix Determinant:")
				print("Matrix1 :",det(matrix1))
				print("Matrix2 :",det(matrix2))
				
				print()
				
				print("Matrix Eigenvalues and Eigenvectors:")
				eig_vals1, eig_vecs1 = eig(matrix1)
				print("Matrix1 :")
				for i in range(len(eig_vals1)):
					print("Eigenvalue:", eig_vals1[i])
					print("Eigenvector:", eig_vecs1[:, i])
				
				print()
				
				eig_vals2, eig_vecs2 = eig(matrix2)
				print("Matrix2 :")
				for i in range(len(eig_vals2)):
					print("Eigenvalue:", eig_vals2[i])
					print("Eigenvector:", eig_vecs2[:, i])

			if operation in '2':
			
				print()

				print("Matrix Transpose:")
				print(matrix1.T)

				print()

				print("Matrix Inverse:")
				try:
					inv_matrix1 = inv(matrix1)
					print(inv_matrix)
				except np.linalg.LinAlgError:
					print("Matrix is not invertible.")
				
				print()

				print("Matrix Determinant:")
				print(det(matrix1))

				print()

				print("Matrix Eigenvalues and Eigenvectors:")
				eig_vals1, eig_vecs1 = eig(matrix1)
				for i in range(len(eig_vals1)):
					print("Eigenvalue:", eig_vals1[i])
					print("Eigenvector:", eig_vecs1[:, i])


		def menu():
				print()
				print("=== Linear Algebra Calculator ===")
				print("Enter '1' for matrix addition, subtraction, multiplication and all of the below functions")
				print("Enter '2' for matrix transpose, inverse, determninat and eigenvalues and eigenvectors")
				print("Enter 'q' to quit")
				print()

		menu()

		while True:
			print()
			operation = input("Enter operation (m for menu) : ")

			if operation == 'q':
				break

			elif operation in '1':
				matrix1 = input("Enter the first matrix (rows separated by ';', columns separated by ','): ")
				matrix2 = input("Enter the second matrix (rows separated by ';', columns separated by ','): ")
				matrix1 = [list(map(parser_value, row.split(','))) for row in matrix1.split(';')]
				matrix2 = [list(map(parser_value, row.split(','))) for row in matrix2.split(';')]
				matrix_operations(matrix1, operation, matrix2)
		
			elif operation in '2':
				matrix1 = input("Enter the matrix (rows separated by ';', columns separated by ','): ")
				matrix1 = [list(map(parser_value, row.split(','))) for row in matrix1.split(';')]
				matrix_operations(matrix1, operation)
		
			elif operation in 'm':
				menu()
		
			else:
				print("Error: Invalid operation")

	if option == 's':
		scientific_calculator()
	elif option == 'v':
		vector_calculator()
	elif option == 'g':
		graphing_calculator()
	elif option == 'l':
		matrix_calculator()

def clear_screen():
	# Clear the terminal screen
	if os.name == 'nt':  # For Windows
		_ = os.system('cls')
	else:  # For Linux and Mac
		_ = os.system('clear')

def main():
	while True:
		clear_screen()
		print("=== Calculator ===")
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
			for i in range(3,0,-1):
				print("Exiting in ",i)
				time.sleep(0.8)
				clear_screen()
			break

		elif option == 'cls':
			clear_screen()

		elif option in 'svgl':
			calculator(option)

		else:
			print("Error: Invalid Input")

if __name__ == '__main__':
	clear_screen()
	main()
