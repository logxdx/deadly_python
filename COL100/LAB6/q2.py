def is_symmetric(A):
	# A is a list of lists 
	# return True or False based on whether A is symmetric
    for i in range(len(A)):
        for j in range(i+1):
            if a[i][j]==a[j][i]:
                flag=True
            else:
                return False
    return flag
