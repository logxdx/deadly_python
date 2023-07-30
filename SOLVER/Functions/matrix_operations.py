import numpy as np

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
		operation = input("Enter operation (mn for menu) : ")

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
		
		elif operation in 'mn':
			menu()
		
		else:
			print("Error: Invalid operation")

matrix_calculator()