def text1():
    print('text1开始了')
    print('text1结束啦')


def text2():
    print('text2开始了')
    text1()
    print('text2结束了')


text2()


# 定义函数求n-m之间所有的整数之和
def all4(n, m):
    result = 0
    for i in range(n, m):
        result = result + i
    return result


print(all4(1, 100))


# 求一个数的阶乘
def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


print(factorial1(5))


# 计算m阶乘的和  m = 6 ===> 1!+2!+3!+4!+5!+6!
def factorial2(n):
    sum = 0
    x = 1
    for i in range(1, n + 1):
        x *= i
        sum += x
    return sum


print(factorial2(5))  # 153


def fac_sum(m):
    x = 0
    for i in range(1, m + 1):
        x += factorial1(i)
    return x


print(fac_sum(5))  # 153
