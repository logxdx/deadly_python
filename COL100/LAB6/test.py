import math, numpy as np
import matplotlib.pyplot as plt
print(math.e)
print(np.e)

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


print("||Example: a*(log(b*x))/(log(base))||\n||Base is greater than 0 and not equal to 1||")
base = eval(input("Enter the base of the logarithm (base): ").replace('pi', 'math.pi').replace('e','math.e'))
coefficient = eval(input("Enter the coefficient (a): ").replace('pi', 'math.pi').replace('e','math.e'))
coeff = eval(input("Enter the multiplier coefficient (b): ").replace('pi', 'math.pi').replace('e','math.e'))
			
def logarithmic_function(x):
    return float(coefficient) * np.log(coeff*x+x**2) / np.log(base)

start = float(input("Enter the starting x value: "))
end = float(input("Enter the ending x value: "))
num_points = int(input("Enter the number of points to plot: "))
plot_function(logarithmic_function, start, end, num_points)
