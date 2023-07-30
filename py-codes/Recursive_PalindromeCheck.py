#1
def palin_check(s, l, r):
    if l >= r:
        return True
    if l == r:
        return True 
    
    if s[l] == s[r]:
        return palin_check(s, l+1, r-1)
    else:
        return False


#2
def ispalin(s):
    if len(s)==1:
        return True
    elif len(s)==2:
        if s[0]==s[1]:
            return True
    if s[0]==s[-1]:
        return ispalin(s[1:-1])
    else:
        return False

s='abcba'
print(ispalin(s))
print(palin_check(s,0,len(s)-1))
