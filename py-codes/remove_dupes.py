l=[9,8,9,8,7,6,8,8,5,4,1,1,2,2,1,5,3,3,4,4,5,0,10,56,75,90,99,100,5,6,6,7,7,8,8]
i,n = 0,len(l)

while i < n:
    val=l[i]
    count=l.count(val)
    if count>1:
        for i in range(count-1):
            l.remove(val)
    n-=count-1
    i+=1
l.sort()
print(l)