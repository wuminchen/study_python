import time


def cal_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('代码耗时', end - start)

    return inner


@cal_time  # 1,调用cal_time().  2,把被装饰的函数传递给fn
def demo():
    print('hello')
    time.sleep(5)
    print('world')


# 3。再次调用demo函数时候，不再是原来的demo函数，而是inner函数了
demo()
