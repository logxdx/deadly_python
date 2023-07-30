a=float(input())
b=float(input())
c=float(input())

D=b**2 - 4*a*c

if a==0:
    print("Not a valid quadratic equation")
elif D<0:
    print("No real roots")
elif D==0:
    print(-b/(2*a))
else:
    r1=(-b-D**(0.5))/(2*a)
    r2=(-b+D**(0.5))/(2*a)
    print(r1,r2)