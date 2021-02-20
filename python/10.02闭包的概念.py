# 　闭包的基本概念
def outer():
    x = 10  # 在外部函数里定义了一个变量x,是一个局部变量

    def inner():
        # 在内部函数如何修改外部函数的局部变量
        nonlocal x  # 此时，x不是新增变量，而是外部的局部变量x

        y = x + 1
        x = 20  # 新定义的内部函数
        print(y)

    return inner


outer()()  # y = 11 # 调用内部函数
