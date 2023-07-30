import time

f1=open(r"E:\OneDrive - IIT Delhi\CODE\Deadly_Python\Results\Primes.txt","w+")
pad,count,p=20,0,[]
q=[]
strprime = ''

u=int(input('Enter the upper limit : '))
l=int(input('Enter the lower limit (min 2) : '))

start = time.time()

if l<u:
    for num in range(l,u+1):
        for i in range(2,int(num**0.5) +1):
            if num%i==0:
                break
        else:
            q.append(num)
            strprime+=f'{num}\n'
            count+=1
else:
    print('Lower limit can\'t be greater than the upper limit')

end = time.time()

print(q)
print('There are',count,'prime numbers in the range',l,'to',u)
print("Time taken :",end-start)

f1.writelines(strprime)
f1.write(f'\nTime Taken : {end-start}\n')
f1.flush()
f1.close()
