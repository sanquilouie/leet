from functools import lru_cache



# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(6))
# # print(fib.cache_info())
#
cache = {}
@lru_cache(maxsize=1000)
def fibo(n):
    if n in cache:
        return cache[n]
    elif n < 2:
        cache[n] = n
        return cache[n]
    else:
        cache[n] = fibo(n - 1) + fibo(n - 2)

        return cache[n]


x = fibo(5)
print(cache)
print(x)