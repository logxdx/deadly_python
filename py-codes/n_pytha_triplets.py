def pytrips(n):
    res=[]
    pad=5
    f1=open(r"E:\OneDrive - IIT Delhi\CODE\Deadly_Python\Results\PythaTrips.txt","w+")

    for i in range(1,2000):
        for j in range(1,i):
            if i**2+j**2==n**2:
                res.append(str([j,i,n]).rjust(pad))
            elif i**2-j**2==n**2:
                res.append(str([min(j,n),max(j,n),i]).rjust(pad))
    
    if res==[]:
        print("No pythagorean triples with "+str(n))
    else:
        print(*res)

    f1.writelines(res+['\n'])
    f1.flush()
    f1.close()

for i in range(int(input())):
    pytrips(i)