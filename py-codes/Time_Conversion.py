def timeConversion(s):
    # Write your code here
    tc=list(s)
    if tc[-2]=='P':
        tc.pop()
        tc.pop()
        hh=int(tc[0])*10+int(tc[1])
        if hh!=12:
            hh+=12
            del tc[:2]
            tc.insert(0,str(hh))
            
    else:
        tc.pop()
        tc.pop()
        if tc[0]=='1' and tc[1]=='2':
            tc[0]='0'
            tc[1]='0'        
    return "".join(tc)


print(timeConversion('01:40:22PM'))