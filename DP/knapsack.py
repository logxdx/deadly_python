
def knapsack(v,w,capacity,dp):
    n=len(w)

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if w[i - 1] <= j:
                weight = w[i-1]
                value=v[i-1]
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]

    i, j = n, capacity
    items = []
    while i >0 and j>0 :
        if dp[i][j] != dp[i-1][j]:
            items.append(v[i-1])
            j -= w[i-1]
        i-=1

    return dp[n][capacity],items



#######################################################################################
w = [2, 3, 4, 1, 5]
v = [3, 4, 5, 2, 6]
capacity = 7

dp = [[0] * (capacity + 1) for _ in range(len(w) + 1)]

print(*knapsack(v,w,capacity,dp))

dp.insert(0,['w\c',0]+[i for i in range(1,capacity+1)])
dp[1].insert(0,'0 |')
j = 0
for i in dp[2:]:
    i.insert(0,str(w[j])+' |')
    j += 1

for i in dp :
    for j in i:
        print(str(j).rjust(3),end= ' ')
    print()


'''
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # Finding the items included in the knapsack
    included_items = []
    i = n
    j = capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            included_items.append(values[i - 1])
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], included_items[::-1]

# Example usage
weights = [2, 3, 4, 1, 5]
values = [3, 4, 5, 7, 6]
capacity = 7

max_value, included_items = knapsack_01(weights, values, capacity)
print("Maximum value:", max_value)
print("Included items:", included_items)
'''
