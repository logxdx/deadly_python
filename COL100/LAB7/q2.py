def lbsearch(arr, x):
    l,r=0,len(arr)-1
    index=-1
    while r>=l:    
        mid=(l+r)//2
        if arr[mid]>=x:
            r=mid-1
        else:
            l=mid+1

        if arr[mid]==x:
            index=mid
    return index


def rbsearch(arr, x):
    l,r=0,len(arr)-1
    index=-1
    while r>=l:        
        mid=(l+r)//2
        if arr[mid]<=x:
            l=mid+1                
        else:
            r=mid-1

        if arr[mid]==x:
            index=mid
    return index


def first_and_last(L, x):
    first=lbsearch(L, x)
    second=rbsearch(L, x)
    return (first,second)
