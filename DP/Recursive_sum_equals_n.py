def subset_sum(L, k):
    # Recursive helper function to find the subset with the given sum
    
    def find_subset(current_sum, index, subset):
        # Base cases
        if current_sum == k:
            return True, subset
        if current_sum > k or index >= len(L):
            return False, []
        
        # Include the current element in the subset
        include_result = find_subset(current_sum + L[index], index + 1, subset + [L[index]])
        if include_result[0]:
            return include_result
        
        # Exclude the current element from the subset
        exclude_result = find_subset(current_sum, index + 1, subset)
        if exclude_result[0]:
            return exclude_result
        
        # If neither inclusion nor exclusion leads to a valid subset, return False
        return False, []

    # Call the recursive function starting from index 0 with an empty subset
    return find_subset(0, 0, [])

L = [7, 3, 2, 5, 8]
k = 14

result = subset_sum(L, k)
print(result)  # Output: (True, [7, 2, 5])

L , k = [7, 3, 2] , 11
print(subset_sum(L,k))
