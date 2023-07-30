def uncommon_words(s1, s2):
    ucommon=[]
    ds1=dict(zip(s1.split(),[s1.split().count(i) for i in s1.split()]))
    ds2=dict(zip(s2.split(),[s2.split().count(i) for i in s2.split()]))
    
    for i in ds1.keys():
        if ds1[i]==1:
            if i not in ds2.keys():
                ucommon.append(i)
    
    for i in ds2.keys():
        if ds2[i]==1:
            if i not in ds1.keys():
                ucommon.append(i)
    
    return (ucommon)
