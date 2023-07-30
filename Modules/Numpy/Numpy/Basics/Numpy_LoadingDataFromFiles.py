import numpy as np

a = np.genfromtxt(
    r"E:\OneDrive - IIT Delhi\CODE\Deadly_Python\FUNCTIONS\Numpy\Numpy\Basics\input.txt", dtype=int, delimiter=',')
print(a)

# advanced indexing, Boolean Masking and indexing
print(a > 50)
print(a[a > 50]),
# you can index with a list in NumPy
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(b[[0, 1, 3, 5]])
print(np.any(a > 50, axis=0))