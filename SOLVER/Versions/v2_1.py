# Author: Karan Deo Burnwal
# Updated on: 18/05/2023_01:16
'''
In this updated code, the solve_differential_equation() function is modified to handle mathematical constants. 
It replaces occurrences of 'pi' with math.pi and 'e' with math.e using the replace() method. This allows you to use these constants in your differential equation inputs.
Now you can use mathematical constants such as 'pi' or 'e' in your differential equations. 
For example, you can enter ''dy/dx = 2 * math.pi * x'' or ''dy/dx = math.e ** x'' in the differential equation input.
'''
# DIFFERENTIAL SOLVER NOT WORKING


import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

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
	x = np.linspace(-10, 10, 400)
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

def solve_differential_equation(): #ERROR
    print("=== Differential Equation Solver ===")
    print("Enter a differential equation in the form 'dy/dx = f(x, y)'")
    print("Example: 'dy/dx = x**2 - y'")
    print("Enter 'q' to quit")

    equation = input("Enter a differential equation: ")

    if equation == 'q':
        return

    try:
        # Extract the equation components
        equation = equation.replace('^', '**')  # Allowing '^' as a power operator
        equation = equation.replace('=', '-')  # Convert '=' to '-' for odeint
        equation = equation.replace('pi', 'math.pi')  # Replace 'pi' with math.pi
        equation = equation.replace('e', 'math.e')  # Replace 'e' with math.e

        # Parse the equation to define the function f(x, y)
        exec("def f(x, y): return " + equation)

        # Prompt for initial conditions
        initial_condition_x = float(input("Enter the initial x: "))
        initial_condition_y = float(input("Enter the initial y: "))

        # Prompt for the range of x values
        start_x = float(input("Enter the starting x value: "))
        end_x = float(input("Enter the ending x value: "))
        num_points = int(input("Enter the number of points to plot: "))

        # Generate x values
        x = np.linspace(start_x, end_x, num_points)

        # Solve the differential equation
        y = odeint(f, initial_condition_y, x)

        # Plot the solution
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Solution of ' + equation)
        plt.grid(True)
        plt.show()

    except Exception as e:
        print("Invalid equation or input:", e)

def main():
    while True:
        print("=== Calculator ===")
        print("Enter 'b' for basic calculator")
        print("Enter 's' for scientific calculator")
        print("Enter 'v' for vector calculator")
        print("Enter 'g' for graphing calculator")
        print("Enter 'd' for differential equation solver")
        print("Enter 'q' to quit")

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
        elif option == 'd':
            solve_differential_equation()

if __name__ == '__main__':
    main()
