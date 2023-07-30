def get_intersection(A, B, C):
    common_elements = []
    i = j = k = 0

    while i < len(A) and j < len(B) and k < len(C):
        if A[i] == B[j] == C[k]:
            common_elements.append(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] <= B[j] and A[i] <= C[k]:
            i += 1
        elif B[j] <= A[i] and B[j] <= C[k]:
            j += 1
        else:
            k += 1

    return common_elements
