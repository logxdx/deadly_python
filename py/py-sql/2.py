def empty(stk):
    if stk==[] :
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)

def display(stk):
    if empty(stk):
        print("\nEmpty stack !!")
    else:
        top=len(stk)-1
        print(stk[top],"<---TOP" )
        for i in stk[top-1:0:-1]:
            print(i)

####### MAIN PROGRAM #######

Stack=[]
top=None

while True :
    
    print("\n||Employee Management||")
    print("\n1.Enter employee details ")
    print(" 2.Display all employee details ")
    print(" 3.Exit ")

    ch=int(input("\nEnter your choice : "))    
    
    if ch==1:

        n=int(input("\nHow many details do you wish to enter : "))
        for i in range(n) :
            item=input("\nEnter details for employee "+str(i+1)+" : ")
            push(Stack,item)

    elif ch==2:
        print("Empno,Name")
        display(Stack)

    elif ch==3:
        break

    else:
        print("\nInvalid input\n")