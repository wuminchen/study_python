# *args表示可变位置参数
# **kwargs 表示可变关键字参数
def add(a, b, *args, mul=1, **kwargs):  # *args表示可变参数
    print(a, b)
    print(args)  # 多出的参数会以元祖的形式保存到args里
    print(kwargs)  # 多出来的关键字参数以字典的形式保存 关键字参数：在函数定义时，为参数设置了默认值，我们叫它关键字参数。
    c = a + b
    for arg in args:
        c = c + arg
    return c * mul


print(add(245, 6, 5, 6, 5, x=1, y=2, mul=2))
