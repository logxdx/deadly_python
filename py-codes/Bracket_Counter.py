def parser(expression):
    brakets=[]
    balanced=True

    for i in expression:
        if i =="(":
            brakets.append(i)
            balanced=False
        elif i==")":
            brakets.pop()

    if brakets==[]:
        balanced=True
    else:
        balanced=False

    return balanced


L=input("Enter brackets : ")
print(parser(L))
