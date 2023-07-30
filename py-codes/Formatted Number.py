

def print_formatted(number):
    # your code goes here
    pad=len(bin(number))
    for i in range(1,number+1):
        oc=str(oct(i)[2:])
        he=str(hex(i)[2:]).upper()
        bi=str(bin(i)[2:])
        print(str(i).rjust(pad),oc.rjust(pad),he.rjust(pad),bi.rjust(pad))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
