def rem_dupes(l=[1,1,5,5,4,2,7,8,4,3,3]):
    n=len(l)-1
    i=0
    while i<n:
        for j in range(n,i,-1):
            if l[j]==l[i]:
                l[j]=l[n]
                n-=1
        i+=1    

    print(l[:i])

rem_dupes()