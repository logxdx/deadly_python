def fourth_smallest(l):
    for i in range(4):
        min_index=i
        for j in range(i+1,len(l)):
            if l[j]<l[min_index]:
                min_index=j
        l[i],l[min_index]=l[min_index],l[i]

    return l[3]
