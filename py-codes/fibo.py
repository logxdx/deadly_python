n=int(input())
a,b,fibo=0,1,[]
for i in range(n//2+1,0,-1):
    fibo.extend([a,b])
    a=a+b
    b=a+b
print(fibo[n])
print("Count of fibonacci numbers :",n)
