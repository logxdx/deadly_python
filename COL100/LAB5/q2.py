def final_balance(t):
    final=0
    for i in t:
        if i[0]=='D':
            final+=int(i[2:])
        if i[0]=='W':
            if final<int(i[2:]):
                return -1
            final-=int(i[2:])
    return final
