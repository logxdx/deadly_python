#python 3.7.1

print ("Hello, Dcoder!")




a=[
   [1,2,3],
   [4,5,6],
   [7,8,9]
  ]
print("Original Matrix")

for r in range(0,len(a)):
    for c in range(0,len(a[0])):
        print(a[r][c], end=' ')
    print()



print()    




print("Transposed Matrix")
for r in range(0,len(a)):
    for c in range(0,len(a[0])):
        print(a[c][r], end=' ')
    print()