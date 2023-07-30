def Check_single_drop(L):
	i=0
	l=len(L)
	while i<=l-3:        
		if L[i]<L[i+1]:	
			for j in range(i+1,l-2):
				if L[j]>L[j+1]:
					return False
		i+=1

	else:
		return True


L=[3,2,1,3,3,2]
print(Check_single_drop(L))
