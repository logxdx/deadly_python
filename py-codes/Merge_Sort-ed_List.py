def merge(l1,l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    else:
        hd1,tl1 = l1[0],l1[1:]
        hd2,tl2 = l2[0],l2[1:]
        if hd1<hd2:
            return [hd1] + merge(tl1,l2)
        else:
            return [hd2] + merge(l1,tl2)

print(merge([1,3,5,7,9],[2,4,6,8,10]))