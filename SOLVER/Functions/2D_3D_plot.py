import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class plot_function():
	def __init__(self) -> None:
		pass

	def graph_function_parser(self,s):						# Converting input to differentiable and integrable form
		s=s.replace('sqrt','np.sqrt').replace('e^','(np.e)**').replace("pi","np.pi")
		s=s.replace('sin','np.sin').replace('anp.sin','np.asin')
		s=s.replace('csc','1/np.sin').replace('a1/np.sin','1/np.asin')
		s=s.replace('cos','np.cos').replace('anp.cos','np.cos')
		s=s.replace('sec','1/np.cos').replace('a1/np.cos','1/np.acos')
		s=s.replace('tan','np.tan').replace('anp.tan','np.atan')
		s=s.replace('cot','1/np.tan').replace('a1/np.tan','1/np.atan')
		s=s.replace('log', 'np.log').replace('abs', 'np.abs').replace('^','**')

		return (s)

	def plot_function(self):
		
		while True:
				def plot_2d_function(expression, x_range):
					x = np.linspace(x_range[0], x_range[1], 2000)
					y = eval(expression)

					plt.plot(x, y)
					plt.xlabel('x')
					plt.ylabel('y')
					plt.title('2D Function Graph')
					plt.grid(True)

				def plot_3d_function(expression, x_range, y_range):
					
					x = np.linspace(x_range[0], x_range[1], 1000)
					y = np.linspace(y_range[0], y_range[1], 1000)
					x, y = np.meshgrid(x, y)
					Z = eval(expression)

					fig = plt.figure()
					ax = fig.add_subplot(111, projection='3d')
					ax.plot_surface(x, y, Z)
					ax.set_xlabel('x')
					ax.set_ylabel('y')
					ax.set_zlabel('z')
					ax.set_title('3D Function Graph')

				expression = input("Enter the type of plot (2D or 3D): ")

				if expression == 'q':
					break
				
				if expression.lower() == '2d':
					while True:
						n = input("Enter the number of functions to plot : ")
						if n == 'q':
							break
						else:
							try:
								n = int(n)
								for i in range(n):
									expression = input("Enter function : ")
									expression =  self.graph_function_parser(expression)
									x_range = tuple(map(float, input("Enter the range of x (start <space> end): ").split()))
									plot_2d_function(expression, x_range)
								
								plt.show()
							
							except Exception as e:
								print("Error :",e)
								continue
						plt.show()

				elif expression.lower() == '3d':
					while True:
						n=input("Enter the number of functions to plot : ")
						if n == 'q':
							break
						
						else:
							try:
								n = int(n)
								for i in range(n):
									expression = input("Enter function : ")
									expression =  self.graph_function_parser(expression)
									x_range = tuple(map(float, input("Enter the range of x (start end): ").split()))
									y_range = tuple(map(float, input("Enter the range of y (start end): ").split()))
									plot_3d_function(expression, x_range, y_range)
								plt.show()
							
							except Exception as e:
								print("Error :",e)
								continue

				else:
					print("!! Invalid expression. The expression should contain '2D' or '3D'!!")


p = plot_function()

p.plot_function()