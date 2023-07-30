def get_fashionably_late(students):
    res=[]
    k=(len(students)+1)//2
    for i in range(k,len(students)-1):
        res.append(students[i])
    return(res)
