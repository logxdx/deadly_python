str=input('Enter a string')
words=str.split()

newwords=[word[::-1] for word in words]

str1=' '.join(newwords)

print(str1)
