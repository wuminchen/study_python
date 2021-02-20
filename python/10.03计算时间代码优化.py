import time


def cal_time(fn):
    start = time.time()
    fn()
    end = time.time()
    print('运行时间{}'.format(end - start))


def demo():
    print('hello')
    time.sleep(5)
    print('world')


def foo():
    x = 1
    for i in range(1, 98900000):
        x = x + i
    print(x)


cal_time(demo)
cal_time(foo)
