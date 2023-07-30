import pickle

f=open("Students.dat","wb+")

n=int(input("Enter the Number of Students : "))

for i in range(n):
	rec={}
	print("Student Record ",(i+1),"-----------------")
	name=str(input("Name of the Student : "))
	roll=int(input("Roll No. of the Student : "))
	marks=int(input("Marks of Student : "))
	rec['Name'],rec['Marks'],rec['Roll']=name,marks,roll
	pickle.dump(rec,f)

f.close ()


with open("Students.dat",'rb') as g:
	print(" Student details are as follows :")
	for i in range(n):
		s=pickle.load(g)
		print(s)
	


with open("Students.dat",'rb+') as h:
	k=int(input("Enter the roll no to update marks : "))
	for i in range(n):
		pos=h.tell()
		s=pickle.load(h)
		
		if s['Roll']==k:
			s['Marks']=int(input("Update Marks :"))
			h.seek(pos)
			pickle.dump(s,h)
			break
	else:
		print('**--Invalid Input, No records updated--**')


with open("Students.dat",'rb') as k:
	print(" Student details are as follows :")
	for i in range(n):
		s=pickle.load(k)
		print(s)