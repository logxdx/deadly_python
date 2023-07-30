def selection_sort(l):
    for i in range(len(l)):
        min_index=l.index(min(l[i:]))
        l[i],l[min_index]=l[min_index],l[i]

    print("selection sort :",l)

l=[10,9,1,8,4,3,2,5,6,7]
selection_sort(l)