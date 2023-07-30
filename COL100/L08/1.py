l1=[]
for i in range(int(input())):
    k=int(input())
    l1.append(k)
res={'Marks':'Frequency'}
for i in l1:
    if i not in res:
        res[i]=l1.count(i)
for i in res:
    print(i,":",res[i])