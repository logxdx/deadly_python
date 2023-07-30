def pascal(n):
    if n==1:
        print([1])
        return [1]
    elif n==2:
        return [1,1]
    else:
        row=[1]+add_adjacent(pascal(n-1))+[1]
        return row

def add_adjacent(row):
    if len(row)==1:
        return []
    else:
        return [row[0]+row[1]]+add_adjacent(row[1:])
