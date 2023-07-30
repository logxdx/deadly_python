
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

basic_calculator()
