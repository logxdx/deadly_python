import math
import numpy as np
import matplotlib.pyplot as plt

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
		print("||Example: a*((base)^(b*x))||\n")
		base = eval(input("Enter the base of the exponential function (base): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		coefficient = eval(input("Enter the coefficient (a): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))
		b = eval(input("Enter the multiplier coefficient (b): ").replace('pi', 'math.pi').replace('e','math.e').replace('^','**'))

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
		print("Enter 'c' to plot custom plotting of functions")
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

graphing_calculator()
