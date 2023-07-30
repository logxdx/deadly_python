#Ignore the comment below 
'''
def timeConversion(s):
    hh = s[:2]
    tod = s[-2:]
    if int(hh.strip('0')) < 12 and tod == 'PM':
        hh = str (int(hh.strip('0')) + 12)
    elif hh == '12' and tod == 'AM':
        hh = '00'
    return hh + s[2:-2]

s=timeConversion('10:50:56PM')
print(s)
'''


def timeConversion(s):
    myList = list(s)
    if myList[-2] == 'P':
        myList.pop()
        myList.pop()
        temp1 = int(myList[0])
        temp2 = int(myList[1])
        total = (temp1*10 + temp2)
        if total != 12:
            total += 12
            del myList[0:2]
            myList.insert(0,str(total))
        
    else:
        myList.pop()
        myList.pop()
        if myList[0] == '1' and myList[1] == '2':
            del myList[0:2]
            myList.insert(0,'0')
            myList.insert(1,'0')
    
    return "".join(myList)


print(timeConversion('12:40:22AM'))
