def print_rangoli(size):

    alphabet = ' abcdefghijklmnopqrstuvwxyz'

    for i in range(size,0,-1):
        c = alphabet[size:i:-1] + alphabet[i:size+1]
        c = '-'.join(c)
        print(c.center((size*4)-3,'-'))'''

    for i in range(0,size-1):
        c = alphabet[size:i+2:-1] + alphabet[i+2:size+1]
        c ='-'.join(c)
        print(c.center((size*4)-3,'-'))

n=int(input())
print_rangoli(n)
