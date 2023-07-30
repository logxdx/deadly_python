def computeGCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd

a = int(input())
b = int(input())

gcd=computeGCD(a, b)
lcm=int(a*b/gcd)
print(lcm)