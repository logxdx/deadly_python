def subset_sum(L, k):
    n = len(L)
    dp = [[False] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j >= L[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - L[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    if dp[n][k]:
        subset = []
        i, j = n, k
        while i > 0 and j > 0:
            if dp[i - 1][j]:
                i -= 1
            else:
                subset.append(L[i - 1])
                j -= L[i - 1]
                i -= 1

        return True, subset[::-1]

    return False, []
