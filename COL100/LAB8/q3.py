# Using Dynamic Programming
def lcs_dp(x, y):

    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    l = [[0] * (n + 1) for _ in range(m + 1)] 

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = 1 if x[i - 1] == y[j - 1] else 0

            l[i][j] = max(l[i - 1][j], l[i][j - 1], l[i - 1][j - 1] + match)

    seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        match = 1 if x[i - 1] == y[j - 1] else 0

        if l[i][j] == l[i - 1][j - 1] + match:
            if match == 1:
                seq = x[i - 1] + seq
            i -= 1
            j -= 1
        elif l[i][j] == l[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return l[m][n], seq
