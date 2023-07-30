def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

m=int(input('Enter the length of the board : '))
n=int(input('Enter the width of the board : '))
print('the number of ways to move from one corner to the to opposite corner is : ', int(fact(m+n-2)/(fact(m-1)*fact(n-1))))