n=int(input())
ans=[0,0,0,1]
init=[0,0,0,1]
for i in range(n-4):
    tnacci=sum(ans)
    ans[0],ans[1],ans[2],ans[3]=ans[1],ans[2],ans[3],tnacci
    init.append(tnacci)

print(*init[:n])