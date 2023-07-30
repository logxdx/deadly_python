def F(x):
    s=len(str(x))
    if x==0:
        return 0
    if x<10:
        return x
    elif s%2==1:
        prod=1
        temp=x
        while temp>0:
            d=temp%10
            prod*=d
            temp//=+10
        return F(prod)
    else:
        sum=0
        temp=x
        while temp>0:
            d=temp%10
            sum+=d
            temp//=10
        return F(sum)

print(F(int(input())))
