def Check_single_drop(L):
    i=0
    l=len(L)
    while i<l-2:        
        if L[i]<L[i+1]:     
            for j in range(i,l-1):
                if L[j]>L[j+1]:
                    return False
        i+=1

    else:
        return True


L=[[1,-1,2,-2],[5,4,2,2,0,2,3,3,2],[1,2,3],[3,2,1]]
for i in L:
    print(Check_single_drop(i))
