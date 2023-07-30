def lsearch(arr, n, x):
	for i in range(n):
		if arr[i] == x:
			return i
	return -1

def bsearch(arr, l, r, x):
	if r >= l:
		mid = l + (r - l) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return bsearch(arr, l, mid-1, x)
		else:
			return bsearch(arr, mid+1, r, x)
	else:
		return -1

arr=[
		'Asansol',
		'Bhopal',
		'Burdwan',
		'Chennai',
		'Delhi',
		'Durgapur',
		'Mumbai',
		'Pune'	    
	]

print(arr)

n=len(arr)

x = input("\nEnter the city to search for: ")

print("\nEnter the search method : ")
ch=input("\n1. Linear Search \n2. Binary Search \n\n\n")

if ch=='1' :
	
	result = lsearch(arr, n, x)

	if result == -1 :
		print("\nElement is not present in array")

	else:
		print("\nElement is present at index ", result)


elif ch=='2' :
	
	result = bsearch(arr, 0, n-1, x)

	if result == -1 :
		print("\nElement is not present in array")

	else:
		print("\nElement is present at index ", result)

else: 
	print("\nInvalid Input \n")

	