def reverse_k_row(A, k):
    i=1
    row=k-1
    while row<len(A):
        A[row].reverse()
        i+=1
        row=i*k-1
    return A
