def count_pairs(w):
    count=0
    for i in range(len(w)):
        for j in range(len(w)):
            if w[i]==w[j][::-1] and i!=j:
                count+=1
    return count//2
