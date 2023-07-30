aList=eval(input("Enter the number sequence as a list : "))

print("\nEnter the algorithm to be used for sorting :- \n")

ch=input("1. Insertion sort \n2. Bubble sort \n\n")

if ch=='1':
	print("\nOriginal list is :",aList)
	for i in range(1,len(aList)):
		key=aList[i]
		j=i-1
		while j>=0 and key<aList[j]:
			aList[j+1]=aList[j]
			j-=1
		else:
			aList[j+1]=key

	k=input("1. Ascending order \n2. Descending order \n\n")
	if k=='1':
		print("\n\nSorted list using Insertion sort in Ascending order is : ",aList)
	elif k=='2':
		aList.reverse()
		print("\n\nSorted list using Insertion sort in Descending order is : ",aList)
	else:
		print("Invalid Input \n")

elif ch=='2':
	n=len(aList)
	print("\nOriginal list :-",aList)
	for i in range(n):
		for j in range(n-i-1):
			if aList[j]>aList[j+1]:
				aList[j],aList[j+1]=aList[j+1],aList[j]
	
	k=input("1. Ascending order \n2. Descending order \n\n")
	if k=='1':
		print("\n\nSorted list using Bubble sort in Ascending order is : ",aList)
	elif k=='2':
		aList.reverse()
		print("\n\nSorted list using Bubble sort in Descending order is : ",aList)
	else:
		print("Invalid Input \n")

else:
	print("Invalid input \n")

