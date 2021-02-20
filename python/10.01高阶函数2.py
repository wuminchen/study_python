# 高阶函数的使用场景：
# 一个函数作为另一个函数的返回值
def test():
    print("我是test函数")
    return 'hello'


def demo():
    print("我是demo函数")
    return test


def bar():
    print("我是bar函数")
    return test()


# x = test()
# print(x)

y = demo()
z = y()  # y()等于text()
print(z)

print('---------------')

a = bar()  # a是字符串
print('---------------')
print(a)

# 2.一个函数作为另一个函数的参数
# sort  filter map

# 3.函数内部再定义一个函数

