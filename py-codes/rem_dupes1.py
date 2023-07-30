def rem_dupes(l=[1,1,5,5,4,4,3,3]):
    n=len(l)-1
    i,j=0,0
    while i<n:
        i+=1
        if l[i]!=l[i-1]:
            j+=1
            l[j]=l[i]
    print(l[:j+1])
    return (j+1)

rem_dupes()