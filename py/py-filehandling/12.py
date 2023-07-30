import csv

with open("Data.csv",'w+') as f:
	w=csv.writer(f,delimiter='|')
	w.writerow([  'USER_ID' , 'PASSWORD'  ])

	for i in range(2):
		print("\nUser Record ",(i+1),"\n-----------------")
		uid=input("User ID : ")
		pas=int(input("Password : "))
		rec=[ uid , pas ]
		w.writerow(rec)

with open("Data.csv",'r+') as f:
	r=csv.reader(f,delimiter='|')
	info=[row for row in r]

	userid=input("\nEnter your User ID : ")
	for i in range(len(info)):
		if info[i][0]==userid:
			print("Your password is : ", info[i][1])