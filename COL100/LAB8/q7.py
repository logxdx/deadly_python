def cutter(n):
	if n in dp.keys():
		return dp[n]
	else:
		for i in range(11,n+1):
			dp[i]=max(dp[i-1],2*dp[i-2],3*dp[i-3],i)

	return dp[n]

dp={1: 1, 2: 2, 3: 3, 4: 4, 5: 6, 6: 9, 7: 12, 8: 18, 9: 27, 10: 36}

c=int(input())
print(cutter(c))
