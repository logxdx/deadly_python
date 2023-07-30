import random
a=random.randint(1,6)
for i in range(1,4):
    print("Chance No. ",i)
    n=int(input(" Enter a number from 1-6: "))
    if n==a :
        print("You Win")
        break
    else:
        print("Wrong Answer")
else:
    print("You Lost \nThe number was ",a)