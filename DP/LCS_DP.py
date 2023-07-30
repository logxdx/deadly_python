
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


a = "abcxdf"
b = "abedf"

# DP table initialisation
l = [[0]*(len(a)+1) for _ in range(len(b)+1)]

for i in list(zip(["Length:","LCS:"],lcs(b,a,l))):
    print(*i)

# IGNORE
# BELOW
# CODE
# DP table modification
l.insert(0,['#',"|"]+[i for i in a])
l[1].insert(0,'-')
l[1][1] = '+'
l[1][2:] = ['-']*len(a)
for i in range(2,len(l)):
    l[i].insert(0,b[i-2])
    l[i][1]='|'
print()

# Print DP TABLE
for i in l:
    print(*i)
