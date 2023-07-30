p=[]
for i in range(int(input())):
    p.append(int(input()))

k=max(p)
for j in range(k):
    for i in range(len(p)):
        if k-p[i]>0:
            print('.',end='')
        else:
            print('*',end='')
    k-=1
    print()
