def newton__raphson(f, df, x0, tol=1e-10):
    x = x0
    while abs(f(x)>tol):
        x = x - f(x)/df(x)
    return x

def f(x):
    return a*x**4+b*x**3+c*x**2+d*x+e

def df(x):
    return 4*a*x**3+3*b*x**2+2*c*x+d

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
th=float(input())
x=int(input())

root = newton__raphson(f, df, x, th)
print(root)
