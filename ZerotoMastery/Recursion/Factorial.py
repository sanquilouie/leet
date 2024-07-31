def findFactorialRecursive(num):
    if num == 1:
        return 1
    return num * findFactorialRecursive(num-1)


def findFactorialIterative(number):
    factorial = 1
    for i in range(number):
        factorial *= i+1
    return factorial


print(findFactorialIterative(5))

print(findFactorialRecursive(5))
