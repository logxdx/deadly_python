def GCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
 
a = int(input())
b = int(input())

if a>b:
    print(GCD(a,b))
else:
    print(GCD(b,a))
