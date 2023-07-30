s=input("Enter a string : ")
count=0
for i in s:
  if i in ('AEIOUaeiou'):
    count+=1
conso=len(s.strip())-count
print("Number of vowels in the string is : ",count)
print("Number of Consonants in the string is : ",conso)