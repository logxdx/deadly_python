import csv

with open("Student.csv",'w+') as f:
	w=csv.writer(f,delimiter='|')
	w.writerow([  'ROLL_NO'  ,  'NAME'  ])

	for i in range(2):
		print("\nUser Record ",(i+1),"\n-----------------")
		rollno=int(input("Roll No : "))
		name=input("Name : ")
		rec=[{rollno:name}]
		w.writerow(rec)

with open("Student.csv",'r+') as f:
	print("\n\n\n")
	r=csv.reader(f,delimiter='|')
	for row in r:
		print(row)