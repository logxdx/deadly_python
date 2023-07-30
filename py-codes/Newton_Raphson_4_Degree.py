def newton_raphson(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            break
        x = x - fx / dfx
    return x

def f(x):
    return a*x**4+b*x**3+c*x**2+d*x+e

def df(x):
    return 4*a*x**3+3*b*x**2+2*c*x+d

a,b,c,d,e=[float(i) for i in input().split()]

root = newton_raphson(f, df, 10000)
print(root)