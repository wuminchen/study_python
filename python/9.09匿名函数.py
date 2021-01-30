def add(a, b):
    return a + b


x = add(4, 5)  # 函数名作用是调用函数，获取函数执行结果，并赋值给变量x

print(x)

fn = add  # 给函数fn起了一个别名
print(fn(4, 5))

# 除了使用def定义一个函数，还可以使用lambda定义一个函数
# 匿名函数，用来表达一个简单函数。只调用一次
# 调用匿名函数的两种方式
# 1、定义一个名字
# 2、把这个函数当做参数传给另一个函数使用
mul = lambda a, b: a * b
print(mul(9, 6))
