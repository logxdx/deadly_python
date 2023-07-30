def binary_search_left(L, x):
        left = 0
        right = len(L) - 1
        index = "ㄟ( ▔, ▔ )ㄏ"

        while left <= right:
            mid = (left + right) // 2

            if L[mid] >= x:
                right = mid - 1
            else:
                left = mid + 1

            if L[mid] == x:
                index = mid

        return index

def binary_search_right(L, x):
        left = 0
        right = len(L) - 1
        index = "ㄟ( ▔, ▔ )ㄏ"

        while left <= right:
            mid = (left + right) // 2

            if L[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1

            if L[mid] == x:
                index = mid

        return index

# Example usage
L = [1, 2, 2, 3, 3, 3, 4, 4, 5]
x = 3
print({i:el for i,el in enumerate(L)})
first_occurrence = binary_search_left(L, x)
last_occurrence = binary_search_right(L, x)
print()
print("{} --> First Occurence at {}, Last Occurence at {}".format(x,first_occurrence,last_occurrence))
print()
print()

# x is not present in the list
L = [1, 2, 2, 3, 3, 3, 4, 4, 5]
x = 6
print({i:el for i,el in enumerate(L)})
first_occurrence = binary_search_left(L, x)
last_occurrence = binary_search_right(L, x)
print()
print("{} --> First Occurence at {}, Last Occurence at {}".format(x,first_occurrence,last_occurrence))
print()
print()


s=[1,5,7,9,12,15,18,18,18,19,20,25,28,37]
x=18
print({i:el for i,el in enumerate(L)})
first_occurrence=binary_search_left(s,x)
last_occurrence=binary_search_right(s,x)
print()
print("{} --> First Occurence at {}, Last Occurence at {}".format(x,first_occurrence,last_occurrence))
print()
