import os
os.system("cls")

# # Using Dynamic Programming
# def longest_common_subsequence(x, y):

#     m = len(x)
#     n = len(y)

#     # declaring the array for storing the dp values
#     l = [[0] * (n + 1) for _ in range(m + 1)] 

#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             match = 1 if x[i - 1] == y[j - 1] else 0

#             l[i][j] = max(l[i - 1][j], l[i][j - 1], l[i - 1][j - 1] + match)

#     seq = ""
#     i, j = m, n
#     while i > 0 and j > 0:
#         match = 1 if x[i - 1] == y[j - 1] else 0

#         if l[i][j] == l[i - 1][j - 1] + match:
#             if match == 1:
#                 seq = x[i - 1] + seq
#             i -= 1
#             j -= 1
#         elif l[i][j] == l[i - 1][j]:
#             i -= 1
#         else:
#             j -= 1

#     return l[m][n], seq


def lcs(x,y,l):
    # Calculate length of LCS
    m,n = len(x), len(y)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                l[i][j] = l[i-1][j-1]+1
            else:
                l[i][j] = max(l[i-1][j],l[i][j-1])

    # Find LCS
    seq=''
    i,j = m,n
    while i>0 and j>0:
        if x[i-1] == y[j-1]:
            seq = x[i-1] + seq
            i-=1
            j-=1
        elif l[i][j] == l[i-1][j]:
            i-=1
        else:
            j-=1
    
    return l[m][n], seq


if __name__ == "__main__":
    a = "abcxdf"
    b = "abedf"
    
    # expected_ln = 3
    # expected_subseq = "abd"

    # ln, subseq = longest_common_subsequence(a, b)
    # print("len =", ln, ", sub-sequence =", subseq)


    l = [[0]*(len(a)+1) for _ in range(len(b)+1)]
    
    for i in list(zip(["Length:","LCS:"],lcs(b,a,l))):
        print(*i)
    
    # DP table modification
    l.insert(0,['#',"|"]+[i for i in a])
    l[1].insert(0,'-')
    l[1][1] = '+'
    l[1][2:] = ['-']*len(a)
    for i in range(2,len(l)):
        l[i].insert(0,b[i-2])
        l[i][1]='|'
    
    print()

    for i in l:
        print(*i)
