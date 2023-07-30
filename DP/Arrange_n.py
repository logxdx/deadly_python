# Returns the number of arrangements to
# form 'n' using recursion
def solveit(n):
    global count
    count+=1
    # Base case
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    return (
            solveit(n - 1) +
            solveit(n - 3) +
            solveit(n - 5) 
            )

# This function returns the number of
# arrangements to form 'n' using memoization
# lookup dictionary/hashmap is initialized

def solveit1(n, lookup = {}):
    global count
    count+=1
    # Base cases
    # negative number can't be
    # produced, return 0
    if n < 0:
        return 0

    # 0 can be produced by not
    # taking any number whereas
    # 1 can be produced by just taking 1
    if n == 0:
        return 1

    # Checking if number of way for
    # producing n is already calculated
    # or not if calculated, return that,
    # otherwise calculate and then return
    if n not in lookup:
        lookup[n] = (
                    solveit1(n - 1) +		
                    solveit1(n - 3) +
                    solveit1(n - 5)
                    )
    return lookup[n]

# Driver Code
if __name__ == "__main__":
    num = int(input())
    print()
    
    count = 0
    print(solveit1(num,{}))
    print(count)

    count = 0
    print(solveit(num))
    print(count)
