import time


def cal_time(fn):
    def inner(n, *args, **kwargs):
        start = time.time()
        s = fn(n)
        end = time.time()
        print("代码耗时", end - start)
        return s

    return inner


@cal_time
def foo(n):
    x = 1
    for i in range(1, n):
        x = x + i
    return x


# 要记住，后边的foo不再是原来的foo，所以原来的foo只有一个参数，而到后边的foo可以有多个参数，因为他们不是同一个，所以参数可以不一样
# 这也是python修饰器强大的一点
# 原来的foo是和fn（）是一伙的，后来的foo是和inner一伙的
foo(100000)

print('------------')

m = foo(10000000)
print(m)
