import pickle

f=open("Items.dat","wb+")
ch='y'

while ch =='y' or ch == 'Y':
	n=int(input("Enter the number of records you want to enter : "))
	for i in range(n):
		rec={}
		print("Item No : ",i+1)
		name=str(input("Item Name : "))
		price=int(input("Item Price : "))
		rec['Item No'],rec['Item Name'],rec['Item Price']=(i+1),name,price,
		pickle.dump(rec,f)
	ch=input("Do you want to Continue ? ( 'y' for YES and 'n' for NO ) ")
	
f.seek(0)
count=0
print("Items with price more than 100 are : ")
try:
	while True:
		s=pickle.load(f)
		if s['Item Price']>=100:
			print(s)
			count+=1
except EOFError:
	f.close()

print(count)