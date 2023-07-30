ones=["ZERO","ONE", "TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
tens=["TEN","ELEVEN","TWELVE","THIRTEEN","FORUTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN","NINETEEN"]

num=input("Enter any number : ")
str1=""

#For single digit
if len(num)==1:
    for i in range(0,len(ones)):
        if int(num)==i:
                   print(ones[i])
#From 10-19
elif len(num)==2 and num[0]=="1":
     for i in range(0,len(tens)):
         if int(num[1:])==i:
                   print(tens[i])
#From 20-99
elif len(num)==2:
    if num[0]=="2":
        str1+="TWENTY"
    if num[0]=="3":
        str1+="THIRTY"
    if num[0]=="4":
        str1+="FORTY"
    if num[0]=="5":
        str1+="FIFTY"
    if num[0]=="6":
        str1+="SIXTY"
    if num[0]=="7":
        str1+="SEVENTY"
    if num[0]=="8":
        str1+="EIGHTY"
    if num[0]=="9":
        str1+="NINTY"
    for j in range(1,len(ones)):
        if int(num[1:])==j:
            str1+=" "+ones[j]
    else:
        print(str1)
