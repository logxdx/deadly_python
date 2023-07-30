def substr(s, l,subs):
	
	if (len(s) < 1):
		
		subs.append(l+s)
	
	uset = set()
	
	for i in range(len(s)):
		if s[i] in uset:
			continue
		else:
			uset.add(s[i])
		
		temp = "";
		if (i < len(s) - 1):
			temp = s[:i] + s[i + 1:]
		else:
			temp = s[:i]
		
		substr(temp, l + s[i],subs)
		
	return subs


def oddcnt(string):
    d={}
    
    for i in string:
        if i not in d:
            d[i]=string.count(i)
    
    odd=0
    for i in d.values():
        if i%2==1:
            odd+=1
    
    return odd


def convert_palindrome(string):
	j=oddcnt(string)
	s=""
	for i in sorted(string):
		if i not in str(s)	:
			s+=i
	
	if len(string)==1:
		return string
	
	if len(string)%2==0:
		if len(string)==2 and string[0]!=string[1]:
			return "Palindromes cannot be formed"
		if j!=0:
			return "Palindromes cannot be formed"
		else:
			res=[i+i[len(i)-1:1:-1] for i in substr(s,"",[])]
			return res
	
	else:
		if j>1:
			return "Palindromes cannot be formed"
		else:
			res=[i+i[len(i)-1:0:-1] for i in substr(s,"",[])]
			return res

print(convert_palindrome('acc'))