# Sorting a list of strings in custom order
def custom_sort(A,n,s,C):
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if str_grt(A[min_ind],A[j],C,s):
                min_ind=j
        A[i],A[min_ind] = A[min_ind],A[i]   
    return A

def str_grt(x,y,C,s):
    for i in range(s):
        if C.index(x[i]) > C.index(y[i]):
            return True
        elif C.index(x[i]) < C.index(y[i]):
            return False
    return False

def cust_sort(L,n,s,C):
    swap = True
    while swap:
        swap =  False
        i,j=1,0
        while i < n and j < s:
            if C.index(L[i-1][j]) > C.index(L[i][j]):
                L[i],L[i-1] = L[i-1],L[i]
                swap = True
                i+=1
            else:
                j+=1
    return L

C , A = ["a","c","b"] , "aa ab bc ba ac cb ba cc bb".split()
res=custom_sort(A,len(A),2,C)
res1=cust_sort(A,len(A),2,C)
print("My sort:",res)
print("Your sort:",res1)
