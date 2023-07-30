alt,up,down=[1,2,4,3,4,4,1,3],0,0
'''
for i in range(int(input())):
    a=int(input())
    alt.append(a)
'''
l,r=0,len(alt)-1
count=0
while l<r:
    while alt[l]<alt[l+1]:
        count+=1
    else:
        if count>=2:
            up+=1
            count=0
    l+=1

l,r=0,len(alt)-1
count=0
while l<r:
    while alt[l]>alt[l+1]:
        count+=1
    else:
        if count>=2:
            down+=1
            count=0
    l+=1

print(up,down)
