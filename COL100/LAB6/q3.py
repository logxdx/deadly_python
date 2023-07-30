def rotate_matrix(A):
	# A is a list of lists
	# return the rotated matrix B (list of lists)
    # <1,1> ->> <1,2>
    # <2,1> ->> <1,1>
    # <2,2> ->> <2,3>
    B=[[0 for _ in range(len(A))] for k in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j]=A[len(A)-j-1][i]
        
    return B
