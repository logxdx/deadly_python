import math
x=float(input())
th=float(input())
cos=1.0
i=1
err=1
while err>th:
    cos+=((-1)**i)*(x**(i*2))/math.factorial(i*2)
    err=x**(i*2+2)/math.factorial(i*2+2)
    i+=1
print(cos)
