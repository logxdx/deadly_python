time=int(input())

hr=time//3600
time=time%3600
min=time//60
time=time%60
sec=time

print("Hours: ",hr)
print("Minutes: ",min)
print("Seconds: ",sec)