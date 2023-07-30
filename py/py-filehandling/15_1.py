aList=eval(input("Enter the number sequence as a list : "))

ch=input("Input 1 for Insertion sort and 2 for Bubble sort ")

if ch=='1':
	print("Original list is :",aList)
	for i in range(1,len(aList)):
		key=aList[i]
		j=i-1
		while j>=0 and key<aList[j]:
			aList[j+1]=aList[j]
			j-=1
		else:
			aList[j+1]=key

	print("Sorted list using Insertion sort is : ",aList)

elif ch=='2':
	n=len(aList)
	print("Original list :-",aList)
	for i in range(n):
		for j in range(n-i-1):
			if aList[j]>aList[j+1]:
				aList[j],aList[j+1]=aList[j+1],aList[j]
	
	print("Sorted list using Bubble sort is : ",aList)

else:
	print("Invalid input")