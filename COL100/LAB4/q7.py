def maxAmt(value,n,i=0):
    if i == n-1:
        return value[i]
    if i == n-2:
        return max(value[i], value[i+1])
    return max(value[i] + maxAmt(value, n, i+2), maxAmt(value, n, i+1))
