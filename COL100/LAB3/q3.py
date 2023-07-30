def arms(n):
    s=0
    temp=n
    dig=len(str(n))
    
    while temp>0:
        d=temp%10
        s+=d**dig
        temp=temp//10

    if s==n:
        print("Armstrong")
    else:
        print("Not Armstrong")

n=int(input())
arms(n)