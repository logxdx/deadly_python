phrase=input()
spaces=phrase.count(" ")
words=len(phrase.split())
lc,uc=0,0
for i in phrase:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
print("Words:",words,'\nSpaces:',spaces,'\nUppercase:',uc,'\nLowercase:',lc)

