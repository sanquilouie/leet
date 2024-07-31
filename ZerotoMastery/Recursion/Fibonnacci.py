def fiboIterative(n):
    f1 = 0
    f2 = 1
    current_fibo = 0
    for i in range(n-1):
        current_fibo = f1 + f2
        f1 = f2
        f2 = current_fibo
    return current_fibo


def fiboRecursive(n):
    while n < 2:
        return n
    return fiboRecursive(n-1) + fiboRecursive(n-2)


print(fiboRecursive(8))
