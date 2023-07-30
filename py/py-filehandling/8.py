import pickle

f=open('Contacts.dat','wb+')
ch='y'
p=0
while ch =='y' or ch == 'Y':
	n=int(input("Enter the number of records you want to enter : "))
	for i in range(n):
		rec={}
		name=str(input("Name of the person : "))
		mnum=int(input("Enter the Mobile Number of the person : "))
		rec['Name'],rec['Mobile No.']=name,mnum
		pickle.dump(rec,f)
	p+=n
	ch=input("Do you want to Continue ? ( 'y' for YES and 'n' for NO ) ")

f.seek(0)

print(" Contact Details are as follows :")
for i in range(p):
	s=pickle.load(f)
	print('',s)
	
f.seek(0)

k=int(input("Enter the Mobile No. to search for : "))
for i in range(p):
	pos=f.tell()
	s=pickle.load(f)
		
	if s['Mobile No.']==k:
			print("Data found ",s)
			break
else:
	print('**-- Data Does Not Exist --**')


f.close()