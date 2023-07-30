stack=[]
newstr=''

item=input("Enter a string :")
item=item.lower()

for i in item :
	stack.append(i)

for i in range(len(stack)) :
	newstr+=stack.pop()

if newstr==item :
	print('Palindrome')

else :
	print('Not a palindrome')