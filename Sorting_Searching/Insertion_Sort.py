def insertion_sort(l):
	for i in range(1,len(l)):
		print()
		key=l[i]
		print(key)
		while i>=1 and key<l[i-1]:
			l[i]=l[i-1]
			i-=1
			print(l)
		else:
			l[i]=key
	
	print("insertion sort :",l)

l=[10,9,1,8,4,3,2,5,6,7]
print(l)
insertion_sort(l)
