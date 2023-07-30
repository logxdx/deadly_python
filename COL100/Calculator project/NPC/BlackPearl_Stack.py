class Stack:
	def __init__(self):
		# Initialise the stack's data attributes
               
		self.li=[]
	
	def push(self, item):
		# Push an item to the stack
		
		self.li.insert(0,item)

	def peek(self):
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
	
		
		if self.is_empty():
			return 'Error'
		else:
			return self.li[0]
                

	def pop(self):
		# Pop an item from the stack if non-empty
		if self.is_empty()==False:
			self.li.pop(0)
		else:
			return False
			
			


	def is_empty(self):
		# Return True if stack is empty, False otherwise
		
		if self.li == []:
			return True 
		return False

	def __str__(self):
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
	
		string= ' '.join(str(i) for i in self.li)
		return string

	def __len__(self):
		# Return current number of elements in the stack
		
		return len(self.li)
	
l=Stack()
print(l.is_empty())
l.push(5)
l.push(6)
l.push(7)
l.peek()
print(l)
print(len(l))
