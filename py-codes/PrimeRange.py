import time

f1=open(r"E:\OneDrive - IIT Delhi\CODE\Deadly_Python\Results\Primes.txt","w+")
pad,count,p=20,0,[]
q=[]

u=int(input('Enter the upper limit : '))
l=int(input('Enter the lower limit (min 2) : '))

begin=time.time()

if l<u:
    for num in range(l,u+1):
        for i in range(2,num//2 +1):
            if num%i==0:
                break
        else:
            q.append(num)
            count+=1
    print('There are',count,'prime numbers in the range',l,'to',u)
else:
    print('Lower limit can\'t be greater than the upper limit')

end=time.time()

f1.writelines(str(q))
f1.flush()
f1.close()

print("Time taken :",end-begin)
