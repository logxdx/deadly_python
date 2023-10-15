import time

f1=open(r"E:\CODE\Deadly_Python\Results\Primes.txt","w+")
pad,count,p=20,0,[]
q=[]

u=int(input('Enter the upper limit : '))
l=int(input('Enter the lower limit (min 2) : '))

begin=time.time()

if l<=u:
    
    if l<=2:
        q.append("2")

    for num in range(l,u+1):

        if num%2==0:
            continue

        for i in range(2,num//2 +1):
            if num%i==0:
                break

        else:
            q.append(num)
            count+=1

    print(f"There are {count} prime numbers in the range {l} to {u}")
    q.append("\n\n")
    q.append(f"There are {count} prime numbers in the range {l} to {u}")

else:
    print('Lower limit can\'t be greater than the upper limit')

end=time.time()

for i in q:
    f1.write(str(i)+"\n")

print("Time taken :",end-begin)
f1.write(f"\nTime taken : {end-begin} seconds")
f1.flush()
f1.close()
