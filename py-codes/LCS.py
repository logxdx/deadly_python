def nlcs(x,y,m,n):
    if m==0 or n==0:
        return 0
    elif x[m-1]==y[n-1]:
        return max(nlcs(x,y,m,n-1),nlcs(x,y,m-1,n),1+nlcs(x,y,m-1,n-1))
    else:
        return max(nlcs(x,y,m,n-1),nlcs(x,y,m-1,n))

def lcs(x,y,m,n):
    if m==0 or n==0:
        return ''
    if x[m-1]==y[n-1]:
        return lcs(x,y,m-1,n-1)+x[m-1]
    else:
        l1,l2=lcs(x,y,m,n-1),lcs(x,y,m-1,n)
        if len(l1)>len(l2):
            return l1
        else:
            return l2
        
a='ALGORITHMIC'
b='ALTRUISTIC'

print(nlcs(a,b,len(a),len(b)))
print(lcs(a,b,len(a),len(b)))
