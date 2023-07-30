# Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):

	global count
	count+=1  
	
	if n == 1:
		print("\t\t\t\t\t Move disk 1 from rod",from_rod,"to rod",to_rod)  
		return

	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)

	print("\t\t\t\t\t Move disk",n,"from rod",from_rod,"to rod",to_rod)

	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

# Driver code

print("\t\t\t\t\t||---------------------------||")

n =int(input("\t\t\t\t\t Enter the number of discs : "))
print()

count=0

TowerOfHanoi(n, 'A', 'C', 'B') 
# A, C, B are the name of rods

print('\n\t\t\t\t\t Number of steps required is : ',count)
