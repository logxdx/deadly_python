def pytrips(n, f):
    res=[]
    pad=5

    for i in range(1,2000):
        for j in range(1,i):
            if i**2+j**2==n**2:
                res.append(str([j,i,n]).rjust(pad))
            elif i**2-j**2==n**2:
                res.append(str([min(j,n),max(j,n),i]).rjust(pad))
    
    if res==[]:
        print("No pythagorean triples with "+str(n))
        res.append("No pythagorean triples with "+str(n))
    else:
        # print(*res)
        print(f"Pythagorean Triples with {n} : ", *res)
        res.insert(0, f"Pythagorean Triples with {n} : ")

    f.writelines(res+['\n'])
    f.flush()

f1=open(r"E:\CODE\Deadly_Python\Results\PythaTrips.txt","w+")
k = int(input("Enter the range : "))
for i in range(k+1):
    pytrips(i, f1)

f1.close()