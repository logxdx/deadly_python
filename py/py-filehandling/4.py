f=open('Sample.txt','r')
print(f.read())
f.seek(0)
lines=f.readlines()
print("\nNumber of lines is :-",len(lines))

f.close()