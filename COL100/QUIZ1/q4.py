x=int(input())

day=x%30
month=(x//30)%12
year=x//360
d,m,y=1,1,1

day+=d
while d+day>30:
    day=d+day-30
    month+=1

month+=m
while month+m>12:
    month=month+m-12
    year+=1
year+=y


print(str(day).rjust(2,'0')+'/'+str(month).rjust(2,'0')+'/'+str(year).rjust(4,'0'))