d={1:'Karan',2:'Akash',3:'Anish',4:'Aayan',5:'Chirag'}
key=list(d.items())
val=list(d.values())
s=input('Enter the value you want to search for : ')

for i in range(0,len(val)):
    if s==val[i]:
        print('The entered value is present in the dictionary :',key[i])
        break
else:
    print('Error! The entered value is not present in the dictionary.')
