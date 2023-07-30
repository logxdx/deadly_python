
def max_value(V):
    n = len(V)

    # Dynamic programming table to store the maximum values
    dp = [0] * n
    dp[0] = V[0]
    dp[1] = max(V[0], V[1])

    # Array to track the selected items
    selected = [[] for _ in range(n)]
    selected[0].append(dp[0])
    selected[1].append(dp[1])

    # Compute the maximum value and selected items using dynamic programming
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + V[i])
        if dp[i] == dp[i-1]:
            selected[i] = selected[i-1]
        else:
            selected[i] = selected[i-2] + [V[i]]
    return dp[-1], selected[-1]


print(max_value([6, 7, 1, 3, 8, 2, 4]))