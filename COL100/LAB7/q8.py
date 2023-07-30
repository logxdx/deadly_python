def sort_colors(A):
    i,j,k=0,0,0
    while i < len(A):
        if A[i] == 'o':
            A[i],A[j] = A[j],A[i]
            i+=1
            j+=1
        else:
            i+=1
    
    k=j
    while j < len(A):
        if A[j] == 'w':
            A[j],A[k] = A[k],A[j]
            k+=1
            j+=1
        else:
            j+=1
    
    return A
