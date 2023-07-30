import json , string
  
f=open("Sample.txt",'r+')
para=f.read()
punc=string.punctuation
f.seek(0)

for i in para:
    if i in punc:
        para=para.replace(i," ")

words=para.split()

freq={}
for w in words:
    if w not in freq:
        freq[w]=para.count(w)
        
print('The file is :',f.read(),'\n')
print('Frequency of each word is as follows :')
print(json.dumps(freq,indent=2))

f.close()