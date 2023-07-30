a=' abcdefghijklmnopqrstuvwxyz'
def alphabet_vector(string):
    string=string.lower()
    v=[0 for _ in range(26)]
    for i in range(1,27):
        if a[i] in string:
            v[i-1]=1
        else:
            v[i-1]=0
    
    return v

def subtract_vector(s1, s2):
    i=alphabet_vector(s1)
    j=alphabet_vector(s2)
    for _ in range(len(i)):
        i[_]=i[_]-j[_]

    return i
