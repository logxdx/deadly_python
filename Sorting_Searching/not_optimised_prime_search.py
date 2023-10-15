# Optimised the linear_prime_search algorithm 😈😈

import time, os, math

MAX_SIZE = 10000001

# isprime[]: isprime[i] is True if number is prime
# prime[]: stores all prime numbers less than or equal to N
# SPF[]: stores smallest prime factor of number
# |||for Exp: smallest prime factor of '8' and '16'
# is '2' so we put SPF[8] = 2, SPF[16] = 2|||
# count: stores the number of prime numbers in less than or equal to N
isprime = [True] * MAX_SIZE
prime = []
count=0

# Function generate all prime numbers less than N in O(n)
def manipulated_seive(N):
	global isprime, prime, count

	# 0 and 1 are not prime
	isprime[0] = isprime[1] = False

	# Fill rest of the entries
	for i in range(2, int(math.sqrt(N)) + 1):
		# If isprime[i] is True then i is prime number
		if isprime[i]:

			# Remove all multiples of i which are
			# not prime by making isprime[j] = False
			# and put the smallest prime factor of j as i
			# this loop runs only one time for numbers which are not prime
			j = i*i
			while j <= N:
					isprime[j] = False		
					j += i


# Driver program to test above function
if __name__ == "__main__":

	os.system('cls')

	N = int(input(f"Find all primes less than (Must be less than {MAX_SIZE-1}) : ")) # Must be less than MAX_SIZE
	
	start=time.time()
	manipulated_seive(N)
	end=time.time()
	
	print()
	print("Time taken :",end-start)

	f1=open(r"E:\CODE\Deadly_Python\Results\not_optimised_fast_Primes.txt","w+")

	for i in range(N+1):
		# put all the prime numbers in prime[]
		if isprime[i]:
			prime.append(i)
			f1.write(f'{i} \n')
			count+=1

	f1.write(f'\nTime Taken : {end-start} \n')
	f1.flush()
	f1.close()
			
	'''
	#Print all prime numbers less than N
	for i in range(len(prime)):
		if prime[i] <= N:
			print(prime[i],end=' ')
		else:
			break
	'''

	# print("Primes :", *prime)
	print()
	print("Number of primes in range",N,"is",count)
