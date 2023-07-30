def GCD(a,b):
    if a%b==0:
        return b
    else:
        return GCD(b,a%b)

a = int(input())
b = int(input())

if a>b:
    print(GCD(a,b))
else:
    print(GCD(b,a))
