def empty(stk):
    if stk==[]:
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)

def pop(stk):
    if empty(stk):
        return "Underflow"
    else:
        item=stk.pop()
        return item

def peek(stk):
    if empty(stk):
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if empty(stk):
        return "Empty stack"
    else:
        top=len(stk)-1
        print(stk[top],"<---TOP \n" )
        for i in stk[top-1::-1]:
            print(i)

####### MAIN PROGRAM #######

Stack=[]
top=None

while True:
    
    print("||STACK OPERATIONS||")
    print("\n 1.Push ")
    print(" 2.Pop ")
    print(" 3.Peek ")
    print(" 4.Display Stack ")
    print(" 5.Exit ")

    ch=int(input("\nEnter your choice : \n"))

    if ch==1:
        
        item=int(input("\nEnter item :"))
        push(Stack,item)

    elif ch==2:
        
        pitem=pop(Stack)
        if pitem=="Underflow":
            print('\nUnderflow! Stack is empty')
        else:
            print('\nPopped item is:', pitem)

    elif ch==3:
        
        item=peek(Stack)
        if item=="Underflow":
            print('\nUnderflow! Stack is empty')
        else:
            print("\nTopmost item is:",item)
    
    elif ch==4:

        display(Stack)

    elif ch==5:
        break

    else:
        print("\nInvalid input\n")