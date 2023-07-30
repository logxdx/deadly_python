import time

def arms(n):
	s=0
	temp=n
	digits=len(str(n))
	while temp>0:
		d=temp%10
		s=s+d**digits
		temp=temp//10
	if s==n:
		print(n,"is an Armstrong number")


k=int(input("Enter the Range: "))
start = time.time()
for i in range(1,k+1):
	arms(i)
end = time.time()

print(end-start)