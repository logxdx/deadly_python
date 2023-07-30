def get_minima(arr):
	l,r=0,len(arr)-1

	while l<r:
		mid=(l+r)//2

		if arr[mid]<arr[mid-1] and arr[mid]<arr[mid+1]:
			return arr[mid]
		elif arr[mid]>arr[mid-1]:
			r=mid-1
		else:
			l=mid+1
	
	return arr[l]
