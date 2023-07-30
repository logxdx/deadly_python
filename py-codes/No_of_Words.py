str=input('Enter a Sentence : ')
words=str.split()
print('Number of words in the sentence are :',len(words))

count=0
vowels='AEIOUaeiou'
for i in str:
    if i in vowels:
        count+=1

print('Number of vowels in the string are :',count)