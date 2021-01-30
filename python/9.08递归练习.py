# 用递归求n!
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(6))


# 使用递归求斐波那契数列第n个数
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))
