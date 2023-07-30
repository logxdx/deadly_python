def concat_chars_nums(chars, n):
    res=[]
    for i in range(1,n+1):
        for j in chars:
            res.append(j+str(i))
    return res
