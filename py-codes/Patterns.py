n=int(input())+1
for i in range(1,n):
    for j in range(0,i):
        print(i,end=' ')
    print()

print("-----")

for x in range(1,n):
    for y in range(0,n-x):
        print(n-x,end=' ')
    print()

print("-----")

for k in range(1,n):
    for a in range(0,k):
        print(2*k-1,end=' ')
    print()

print("-----")

for x in range(1,n):
    for y in range(0,n-x):
        print(2*(n-x)-1,end=' ')
    print()

print("-----")

'''
str=input("Enter a string: ").upper()
print("Pattern below👇👇")
for b in range(1,len(str)+1):
    for c in range(0,b):
        print(str[c],end=' ')
    print()
'''