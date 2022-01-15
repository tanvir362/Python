import time
import sys

# def fib(n):
#     if n == 0: return 0
#     if n == 1: return 1

#     return fib(n-1) + fib(n-2)


# cache = {0: 0, 1: 1}
# def fib(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     if cache.get(n):
#         return cache.get(n)

#     cache[n-1] = fib(n-1)
#     cache[n-2] = fib(n-2)
#     cache[n] = cache[n-1] + cache[n-2]

#     return cache[n]


# cache = {0: 0, 1: 1}
# def fib(n):
#     if n == 0: return 0
#     if n == 1: return 1

#     for i in range(2, n+1):
#         cache[i] = cache[i-1] + cache[i-2]

#     return cache[n]


def fib(n):
    a = 0
    b = 1

    if n == 0: return 0
    if n == 1: return 1

    for i in range(2, n+1):
        tmp = b
        b = a+b
        a = tmp

    return b



# sys.setrecursionlimit(1000020)
# print(sys.getrecursionlimit())

n = int(input("Enter a number: "))

start = time.perf_counter()
result = fib(n)
end = time.perf_counter()
print(result)
print('Execution time:', end-start,'s')