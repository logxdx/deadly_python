def get_triplet(L):
	for i in range(3):
		max_index=i
		for j in range(i+1,len(L)):
			if L[j]>L[max_index]:
				max_index=j

		L[max_index],L[i]=L[i],L[max_index]
	return tuple(L[:3])

L=[19, 5, 8 ,21, 0, 1, 16, 4, 3, 2 ]

print(get_triplet(L))