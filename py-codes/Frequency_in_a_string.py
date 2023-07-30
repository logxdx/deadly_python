import json,string
Sentence=input('Enter a sentence \n----------------\n')
punct=string.punctuation
for i in Sentence:
    if i in punct:
        Sentence.replace(i, ' ')
words=Sentence.split()
alpha=string.ascii_lowercase+string.ascii_uppercase
freq1={}
freq2={}
for w in alpha:
    if w not in freq1:
        fre1=Sentence.count(w)
        freq1[w]=fre1
for w in words:
    if w not in freq2:
        fre2=Sentence.count(w)
        freq2[w]=fre2
print('The sentence is:',Sentence)
print('Frequency of each word is as follows:')
print(json.dumps(freq2,indent=5))
print('Frequency of each letter is as follows:')
print(json.dumps(freq1,indent=5))
