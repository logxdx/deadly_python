import numpy as np

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

vector_calculator()