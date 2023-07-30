def max_value(v, s):
    if len(v)==0:
        return []
    k=None
    for i,el in enumerate(v):
        pick = [v[i]] + max_value(v[i+1:],s[i+1:])
        notpick = [v[i+1]]+max_value(v[(i+1+s[i+1]):],s[(i+1+s[i+1]):])

        if sum(pick)>sum(notpick):
            if k==None or sum(k)<sum(pick):
                k=pick
        else:
            if k==None or sum(k)<sum(notpick):
                k=notpick

    return sum(k),k

v=[4,3,1,2,1]
s=[2,1,1,1]
print(max_value(v,s))