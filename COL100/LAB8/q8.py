def arrange(A):
    L=A[:]
    index_d={}
    index_list=[]
    
    for i in range(len(L)):
        min_index=i
        for j in range(i+1,len(L)):
            if L[min_index]>L[j]:
                min_index=j
        
        L[min_index],L[i]=L[i],L[min_index]  
        index_d.update({L[i]:i+1})
    
    for i in A:
        index_list.append(index_d[i])
    
    return index_list

print(arrange([28, 32, 10, 2, 4]))
print(arrange([10, 8, 15, 12, 6, 20, 1]))