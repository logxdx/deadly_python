l1=[]
for i in range(int(input())):
    k=int(input())
    l1.append(k)
l2=l1[:]
for i in l2:
    while l1.count(i)>1:
        l1.remove(i)
print(l2)
print(l1)