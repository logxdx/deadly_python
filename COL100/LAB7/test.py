def neg_before_pos(L):
	k,l=0,0
	for i in L[:]:
		if i<0:
			L[k]=i
			k+=1
		else:
			L[len(L)-1-l]=i
			l+=1
	L[len(L)-l:]=L[len(L)-l:][::-1]
	return (L)

l=[10, -6, 7, -5, -8, 1, -7, 5]
print(neg_before_pos(l))
