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
