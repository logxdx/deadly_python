def maxAmtRecursive(value, n = 0):
    if n >= len(value):
        return []
    else:
        pick = [value[n]] + maxAmtRecursive(value, n+2)
        notpick = maxAmtRecursive(value, n+1)

        if sum(pick)>sum(notpick):
            value = pick
        else:
            value = notpick
    
    return value

ls=[ 1, 7, 1, 5, 8, 13, 10, 11, 10, 20, 35, 1 ]

value_list = (maxAmtRecursive(ls))
print(sum(value_list),value_list)
