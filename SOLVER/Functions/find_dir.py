import os, fnmatch

def find1(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def find2(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

a=find1('Documentation.txt', 'E:\\')
b=find_all('Documentation.txt', 'E:\OneDrive - IIT Delhi\CODE\Deadly_Python\SOLVER')
c=find2('Documentation.txt', 'E:\OneDrive - IIT Delhi\CODE\Deadly_Python\SOLVER')
print(a)
print(b)
print(c)
