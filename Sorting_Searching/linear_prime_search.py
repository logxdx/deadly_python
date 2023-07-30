import time, os

f1=open(r"E:\OneDrive - IIT Delhi\CODE\Deadly_Python\Results\fast_Primes.txt","w+")

MAX_SIZE = 10000001

# isprime[]: isprime[i] is True if number is prime
# prime[]: stores all prime numbers less than or equal to N
# SPF[]: stores smallest prime factor of number
# |||for Exp: smallest prime factor of '8' and '16'
# is '2' so we put SPF[8] = 2, SPF[16] = 2|||
# count: stores the number of prime numbers in less than or equal to N
isprime = [True] * MAX_SIZE
prime = []
SPF = [0] * MAX_SIZE
count=0
strprime=''

# Function generate all prime numbers less than N in O(n)
def manipulated_seive(N):
	global isprime, prime, strprime, SPF, count

	# 0 and 1 are not prime
	isprime[0] = isprime[1] = False

	# Fill rest of the entries
	for i in range(2, N+1):
		# If isprime[i] is True then i is prime number
		if isprime[i]:
			# put i into prime[] list
			prime.append(i)
			strprime+=f'{i}\n'
			count+=1

			# A prime number is its own smallest prime factor
			SPF[i] = i

		# Remove all multiples of i*prime[j] which are
		# not prime by making isprime[i*prime[j]] = False
		# and put the smallest prime factor of i*Prime[j] as
		# prime[j] [for example: let i = 5, j = 0, prime[j]
		# = 2 [i*prime[j] = 10] so the smallest prime factor
		# of '10' is '2' that is prime[j] this loop runs
		# only one time for numbers which are not prime
		j = 0
		while j < len(prime) and i * prime[j] <= N and prime[j] <= SPF[i]:
			isprime[i * prime[j]] = False
			
			# put the smallest prime factor of i*prime[j]
			SPF[i * prime[j]] = prime[j]

			j += 1

# Driver program to test above function
if __name__ == "__main__":
	N = int(input(f"Find all primes less than (Must be less than {MAX_SIZE-1}) : ")) # Must be less than MAX_SIZE
	
	start=time.time()
	manipulated_seive(N)
	end=time.time()
	
	os.system('cls')
	'''
	#Print all prime numbers less than N
	for i in range(len(prime)):
		if prime[i] <= N:
			print(prime[i],end=' ')
		else:
			break
	'''

	print(prime)
	print("Number of primes in range",N,"is",count)
	print("Time taken :",end-start)
	
	f1.write(strprime)
	f1.write(f'\nTime Taken : {end-start}\n')
	f1.flush()
	f1.close()
