n=[int(i) for i in input()]
odigits=[1,3,5,7,9]
counter=0
for i in n:
    if i in odigits:
        counter+=1
print(counter)