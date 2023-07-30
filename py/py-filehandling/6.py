f=open('Sample.txt','r')
para=f.read()
print(para,' \n')
v,c,uc,lc=0,0,0,0

vow='AEIOUaeiou'
conso='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
for i in para:
	if i.isupper(): uc+=1

	if i.islower(): lc+=1

	if i in vow: v+=1

	if i in conso: c+=1

print("No of vowels are ",v)
print("No of consonants are ",c)
print("No of lower case characters are ",lc)
print("No of upper case characters are ",uc)

f.close()