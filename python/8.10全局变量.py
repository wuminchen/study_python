a = 100  # 全局变量，在 py 文件里都可以访问
word = 'hello'


def text():
    x = 'hello'  # 这个变量在函数内部定义的变量，他是局部变量，只能在函数内部使用
    print(x)
    # 如果局部变量的名称和全局变量同名，在函数内部又定义一个全新的变量
    # 而不是修改全局变量
    a = 10
    print(a)

    # 函数内部想要修改全局变量
    global word  # 使用global对变量进行声明，可以通过函数修改全局变量
    word = 'ok'
    print(word)

    print(locals(), globals())


text()

print(a)
print(word)

# 内置函数 globals(),locals()查看全局变量,和局部变量

# 在 python只有函数能够分割作用域
if 3 > 2:
    m = 'hi'  # 全局变量
