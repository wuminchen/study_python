# 1、区间判断
score = float(input('请输入你的：'))
# 在某些语言里，区间不能连写，需要逻辑运算符来连接
# python里可以使用连续的区间判断
if 60 > score >= 0:
    print('不及格')

# 2、隐式类型转化
if 4:  # if 后面需要一个布尔类型的值。如果不是布尔类型，将自动转换
    print('hello world')

# 3、三元表达式（if....else的简写）
num1 = int(input('请输入一个数'))
num2 = int(input('请再输入一个数字'))
x = num1 if num1 > num2 else num2
