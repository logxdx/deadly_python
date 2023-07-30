s=[1,5,7,9,12,15,18,18,18,19,20,25,28,37]
n=len(s)

# || Different representztions of List s ||

#   k=tuple(zip(s,[i for i in range(len(s))]))
#   k = [[i,el] for i,el in enumerate(s)]
#   k = [(i,el) for i,el in enumerate(s)]
#   k = [{i:el} for i,el in enumerate(s)]
k = { i:el for i,el in enumerate(s) }

def bsearch(arr,l,r,x):
    if r>=l:
        mid=(r+l)//2

        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return bsearch(arr,l,mid-1,x)
        else:
            return bsearch(arr,mid+1,r,x)
    else:
        return -1

x=int(input("Enter the number to search for : "))

result=bsearch(s,0,n,x)
print()
print(k)
print()

if result==-1:
    print("Element not present in array")
else:
    print("Element is present at index ",result)
