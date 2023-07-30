def remove_common(a,b):
    for i in a.copy():
        if i in b.copy():
            a.remove(i)
            b.remove(i)
    return [a,b]
