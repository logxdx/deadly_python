def get_valid_passwords(passwords):
    res=[]
    for i in passwords:
        lcase,num,char=0,0,0
        if len(i)>=6 and len(i)<=12:
            lcase=sum([1 for c in i if c.islower()])
            num=sum([1 for c in i if c.isdigit()])
            char=sum([1 for c in i if c in '$@#'])
            if lcase>0 and num>0 and char>0:
                res.append(i)
    return res
