def merge_sort(l1,l2):
    res=[]
    i,j=0,0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    while (i < len(l1)):
        res.append(l1[i]) 
        i += 1
    while (j < len(l2)):
        res.append(l2[j]) 
        j += 1
    print(*res)    

merge_sort([1,3,5,7,9],[2,4,6,8,10])
