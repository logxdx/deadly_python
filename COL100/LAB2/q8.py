n=input()
l=len(n)
for i in range(l):
    if n[i]!=n[-1-i]:
        print("not a palindrome")
        break
else:
    print("palindrome")
