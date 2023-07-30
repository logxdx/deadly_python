f1=open(r"First.txt","r")
f2=open(r"Second.txt","w+")

a=f1.readlines()
b=[]
l=len(a)

for i in range(0,l):
    if 'A' in a[i]:
        b.append(a[i])

f2.writelines(b)

f1.close()
f2.close()