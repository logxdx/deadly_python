def bubble_sort(l):
    for i in range(len(l)):
        for j in range(1,len(l)):
            if l[j]<l[j-1]:
                l[j],l[j-1]=l[j-1],l[j]            
    print("bubble sort :",l)

l=[10,9,1,8,4,3,2,5,6,7]
bubble_sort(l)