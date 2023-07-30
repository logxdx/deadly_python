import csv

f=open('Employee.csv','w+',newline='')
w=csv.writer(f,delimiter='|')
sum,ch,p=0,'yes',0

w.writerow([  'Emp_Name' , 'Emp_Id' , 'Salary' ])

while ch=='Yes' or ch=='YES' or ch=='yes' :
	n=int(input("Enter the number of records you want to enter : "))
	for i in range(n):
		print("Employee Record ",(i+1),"-----------------")
		name=str(input("Name of the Employee : "))
		empid=int(input("Employee ID : "))
		sal=int(input("Salary of the Employee : "))
		rec=[ name , empid , sal ]
		w.writerow(rec)
		sum+=sal
	p+=n
	ch=input("Do you want to add more records ? (Yes or No) ")

print("No of employees are ",p)
print("Average salary is ",sum/p)

f.close()