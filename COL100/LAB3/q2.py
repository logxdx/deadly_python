a=input()
b=input()
c=''
for i in a:
    if i not in b:
        c+=i
for i in b :
    if i not in a:
        c+=i
print(c)