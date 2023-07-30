import pickle

f=open('Contacts.dat','wb+')
ch='y'

while ch =='y' or ch == 'Y':
	n=int(input("Enter the number of records you want to enter : "))	
	for i in range(n):
		rec={}
		name=str(input("Name of the person : "))
		mnum=int(input("Enter the Mobile Number of the person : "))
		rec['Name'],rec['Mobile No.']=name,mnum
		pickle.dump(rec,f)
	ch=input("Do you want to Continue ? ( 'y' for YES and 'n' for NO ) ")

f.close ()

with open("Contacts.dat",'rb') as g:
	print(" Contact Details are as follows :")
	for i in range(n):
		s=pickle.load(g)
		print(s)
	
with open("Contacts.dat",'rb+') as h:
	k=int(input("Enter the Mobile No. to search for : "))
	for i in range(n):
		pos=h.tell()
		s=pickle.load(h)
		
		if s['Mobile No.']==k:
			print("Data found ",s)
			break
	else:
		print('**-- Data Does Not Exist --**')
