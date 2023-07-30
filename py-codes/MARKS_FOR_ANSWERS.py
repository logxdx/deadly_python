data=[]
marks=[]
ans=['a','c','d','b','a']

n=int(input())

for i in range(n):
    data.append(list(input()))

for i in range(n):
    num=0
    for j in range(len(data[i])):
        if data[i][j].lower()==ans[j]:
            num+=1
    
    marks.append(num)
    
print(*marks)
