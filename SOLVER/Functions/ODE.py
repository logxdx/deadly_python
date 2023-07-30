
from sympy.interactive import printing
from sympy import *
import sympy as sp


# f.diff(x,x) number of times x is written, is the number of time f is differentiated

def function_parser(s):						# Converting input to differentiable and integrable form
	s=s.replace('sqrt','sp.sqrt').replace('e^','exp')
	s=s.replace('sin','sp.sin').replace('asp.sin','sp.asin')
	s=s.replace('csc','sp.csc').replace('asp.csc','sp.acsc')
	s=s.replace('cos','sp.cos').replace('asp.cos','sp.cos')
	s=s.replace('sec','sp.sec').replace('asp.sec','sp.sec')
	s=s.replace('tan','sp.tan').replace('asp.tan','sp.atan')
	s=s.replace('cot','sp.cot').replace('asp.cot','sp.acot')
	s=s.replace('log', 'sp.log').replace('abs', 'sp.Abs').replace('^','**')

	return eval(s)

def anti_parser(s):
    s=s.replace(',', ' =').replace('sqrt','√').replace('**','^').replace('*','×')
    s=s.replace('exp', '𝓮^').replace('x','𝓍').replace('f','𝓯').replace('y','𝓎')

    return s

def differential_equation_generator():
    order=int(input("Enter the order of the differential equation : "))
    
    func = 0
			
    for i in range(order, -1, -1):    
        coefficient = function_parser(input("Enter the coefficient of order {}: ".format(i)))

        if i == 0:
            func += coefficient*f       
        elif i==1:
            func += coefficient*Derivative(f,x)
        else:
            func += coefficient*Derivative(f,(x,i))    

    constant=function_parser(input("Enter the value of the constant : "))

    return func,constant,order

def solution_DE(y,constant,order):
    diffeq = Eq(y,constant)
    soln = dsolve(diffeq, f)
    output_f = anti_parser(str(soln)[3:-1])
    deqn = str(y) + ' = ' + str(constant)
    
    for i in range(order,-1,-1):  
        if i==1:
            deqn = deqn.replace('Derivative(f(x), x)' , "f\'"+"(x)")
        else:
            deqn = deqn.replace(f'Derivative(f(x), (x, {i}))', "f"+"\'"*i+"(x)")
    
    print()
    print("Solution to the differential equation",deqn)
    print()
    print(output_f)

x,y,t,k = sp.symbols('x y t k')
f = sp.Function('f')(x)

y,constant,order=differential_equation_generator()
solution_DE(y,constant,order)

'''
def Ordinary_DE():
    """
    This function provides an interactive ordinary differential equation (ODE) solver.
    It allows the user to enter a differential equation, specify the order, and obtain the solution.
    """

    def menu():
        """
        Displays the main menu for the ODE solver.
        """
        print()
        print("=== Ordinary Differential Equation Solver ===")
        print("Enter '1' to enter a differential equation")
        print("Enter 'q' to quit")

    menu()

    def differential_equation_generator(order):
        """
        Generates the symbolic representation of a differential equation based on user inputs.

        Parameters:
        - order (int): The order of the differential equation.

        Returns:
        - func (sympy expression): The generated differential equation.
        - constant (float): The value of the constant term in the differential equation.
        - order (int): The order of the differential equation.
        """

        print()
        func = 0

        for i in range(order, -1, -1):
            coefficient = parser_value(input("Enter the coefficient of order {}: ".format(i)))

            if i == 0:
                func += coefficient * f
            elif i == 1:
                func += coefficient * Derivative(f, x)
            else:
                x_diff = ()
                for i in range(i + 1):
                    x_diff += (x,)
                func += coefficient * Derivative(f, x_diff)

        constant = parser_value(input("Enter the value of the constant: "))

        return func, constant, order

    def solution_DE(y, constant, order):
        """
        Solves the differential equation and displays the solution.

        Parameters:
        - y (sympy expression): The generated differential equation.
        - constant (float): The value of the constant term in the differential equation.
        - order (int): The order of the differential equation.
        """

        diffeq = Eq(y, constant)
        soln = dsolve(diffeq, f)
        output_f = anti_parser(str(soln)[3:-1])
        deqn = str(y) + ' = ' + str(constant)

        for i in range(order, -1, -1):
            if i == 1:
                deqn = deqn.replace('Derivative(f(x), x)', "f'(x)")
            else:
                deqn = deqn.replace('Derivative(f(x), (x, {}))'.format(i), "f" + "'" * i + "(x)")

        print()
        print("Solution to the differential equation", deqn)
        print()
        print(output_f)
        print()

    operation = input("Enter Expression (q to quit): ")

    while True:

        if operation == 'q':
            break

        if operation == '1':

            x = sp.symbols('x')
            f = sp.Function('f')(x)

            while True:
                print()
                print("Enter 'q' to exit")
                order = int(input("Enter the order of the differential equation: "))

                if order == 'q':
                    break

                y, constant, ordr = differential_equation_generator(order)
                solution_DE(y, constant, ordr)

        else:
            print("Invalid Input!!")
'''