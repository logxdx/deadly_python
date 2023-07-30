MAX_SIZE = 10000
isprime = [True] * MAX_SIZE
prime = []
SPF = [0] * MAX_SIZE

def seive(N):
    global isprime, prime, SPF
    count,prime=0,[]
    isprime[0] = isprime[1] = False

    for i in range(2, N+1):
        if isprime[i]:
            prime.append(i)
            SPF[i] = i
            count+=1
        j = 0
        while j < len(prime) and i * prime[j] <= N and prime[j] <= SPF[i]:
            isprime[i * prime[j]] = False			
            SPF[i * prime[j]] = prime[j]
            j += 1

def range_sum(L,N):
    seive(N)
    tsum=0
    for i in L:
        for j in prime:
            if j<=i[1] and j>=i[0]:
                tsum+=j
    return (tsum)
