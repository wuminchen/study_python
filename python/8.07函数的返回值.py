# 返回值就是函数执行的结果，并不是所有的函数必须要有返回值
def add(a, b):
    c = a + b  # 变量c在外部不可见，只能在函数内部使用
    return c  # 表示一个函数的执行结果


# 获取到add函数的结果，然后再求结果的4次方
result = add(1, 2)
print(result ** 4)

# print 就是一个内置函数
# 如果一个函数没有函数值，它返回的就是None
x = print('hello')
print(x)

age = input("age")
print(age)
