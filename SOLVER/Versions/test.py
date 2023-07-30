from sympy import *
from sympy.abc import x,y

f=Function('f')
g=Function('g')(x)
print(f,f(x),g)
print(type(f))
print(type(f(x)))
print(type(g))
f = sin(x)
g = cos(x)

print(type(f))
# print(type(f(x)))
print(type(g))
