'''
def find_min_boats(N,x):
    left = 0
    right = len(N)-1
    boats = 0
    while left<=right:
        if N[left]+N[right]<=x:
            left+=1
        right-=1
        boats+=1
    return boats

student_weights = [70, 50, 80, 120, 90, 45]
maximum_weight = 150
boats = find_min_boats(student_weights,maximum_weight)
print(boats)


print()


class Max_idx:
    # write your code below
    def __init__(self, R, C, A):
        self.R = R
        self.C = C
        self.A = A

    def find_max_idx(self):
        max_idx = 0
        sum = 0
        for j in range(self.C):
            sum1 = 0
            for i in range(self.R):
                sum1 += self.A[i][j]
            print(j)
            if sum1 > sum:
                print(sum1,sum)
                sum = sum1
                max_idx = j

        return max_idx

# A = [[1,12,3],[5,5,5],[8,9,10],[1,2,3],[1,2,4]]
# R, C = len(A), len(A[0])
R,C = (int(i) for i in input().strip().split(" "))
A = []
for i in range(R):
    A.append([int(i) for i in input().strip().split(' ')])

res = Max_idx(R, C, A)
print(res.find_max_idx())


print()
'''


def rsearch(L,x):
    l = 0
    r = len(L)-1
    index = -1

    while l<=r:
        mid = (l+r)//2
        
        if L[mid]<=x:
            l=mid+1
        else:
            r=mid-1
        
        if L[mid] == x:
            index = mid
        
    return index

def less_elements(n, L, num):
    #Write your code here.
    answer = 0
    if num in L:
        answer = rsearch(L,num) + 1
    else:
        L.append(num)
        L.sort()
        answer = rsearch(L,num)
    return answer

n,L,Q,q = 5, [1,1,2,3,3], 3, [1,3,4]
# n = int(input())
# L = [int(i) for i in input().strip().split(' ')]
# Q = int(input())
# q = [int(i) for i in input().strip().split(' ')]
answer = []
for num in q:
    answer.append(less_elements(n, L, num))
#OUTPUT
print(' '.join(map(str, answer)))
