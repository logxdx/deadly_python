def isomorphic(x, y):
    m,n=len(x),len(y)
    
    if m!=n:
        return False   
    else:
        iso_list=tuple(zip([i for i in x],[i for i in y]))
        
        for i in range(len(iso_list)):       
            isol=iso_list[:i]+iso_list[i+1:]
            a=iso_list[i]

            for j in range(len(isol)):                

                if iso_list[i][0]==isol[j][0]:
                    if iso_list[i][1]!=isol[j][1]:
                        return False
                    
                elif iso_list[i][0]!=isol[j][0]:
                    if iso_list[i][1]==isol[j][1]:
                        return False
        else:
            return True

#print(isomorphic("aab", "xyz"))
#print(isomorphic("aab", "xxy"))
print(isomorphic("abhvsvbs","abhcccbc"))
