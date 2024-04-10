import time

value = int(input("Nth Fibonacci Number : "))
fibonacci_numbers = []

def fibo(n, fibonacci):

    if n < len(fibonacci):
        return fibonacci[n]
    else:
        fibonacci.append(fibo(n-1,fibonacci) + fibo(n-2,fibonacci))
        return fibonacci[n]

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
start = time.time()
k = fibo(value, fibonacci)
end = time.time()
print(f"{k}, time-taken : {end-start}")



def fib(n,fibo):
    if n in fibo.keys():
        return fibo[n]
    else:
        fibo[n]=fib(n-1,fibo)+fib(n-2,fibo)
        return fibo[n]


fibo = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55, 11: 89, 12: 144, 13: 233, 14: 377, 15: 610, 16: 987, 17: 1597, 18: 2584, 19: 4181, 20: 6765}
start = time.time()
k = fib(value, fibo)
end = time.time()
print(f"{k}, time : {end-start}")

