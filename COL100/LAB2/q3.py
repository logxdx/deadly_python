n=int(input())
counter=0
for i in range(1,8):
    for j in range(i):
        if counter>=n or counter>=26:
            break
        print(chr(65+counter),end=' ')
        counter+=1
    print()