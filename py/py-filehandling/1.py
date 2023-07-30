def prime(n):
	
	for i in range(2,n//2+1):
		if n%i==0:
			break	
	else: 
		print(n)


print("Prime numbers between 1 to 100 are :")


for i in range(2,101):

	prime(i)