import os
os.system("cls")

# List initialisation
L = [1, 1, 7, 3, 2, 6, 5, 1, 4, 10]
# subset sum
k = int(input())

# Memoization Code - Minimum subset
def subsum_memo(A,n,d):
    if n in d.keys():
        return d[n]
    if n == 0:
        return []
    elif n < 0:
        return None
    else:
        min_list = []
        for i,el in enumerate(A):
            ls = subsum_memo(A[:i]+A[i+1:],n-el,d)
            if ls != None :
                comb = ls + [el]
                if min_list == [] or len(min_list)> len(comb):
                    min_list = comb
                    d[n] = min_list
    return d[n]

# Return Boolean Code
def subsum(A,n):
    if n == 0:
        return True
    elif n < 0:
        return False
    else:
        for i, el in enumerate(A):
            new_list = A[:i]+A[i+1:]
            rem= n-el
            bool = subsum(new_list, rem)
            if bool:
                return True
    return False

# Return subset list
def subsum_nomemo(A,n):
    if n == 0:
        return []
    elif n < 0:
        return None
    else:
        for i, el in enumerate(A):
            new_list = A[:i]+A[i+1:]
            rem= n-el
            ls = subsum_nomemo(new_list, rem)
            if ls != None:
                comb = ls + [el]
                return comb
    return None


def main():
    
    # Return Boolean 
    print(subsum(L,k))
    
    # Return subset without using memoization
    print(subsum_nomemo(L,k))

    # Return minimum subset using memo
    print("Minimum list:",subsum_memo(L,k,{}))

# Driver Code
if __name__ == "__main__":
    main()
