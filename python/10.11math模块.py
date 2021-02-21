# math模块：数学计算相关的模块


import math

math.factorial(6)  # 求阶乘
math.floor(12.98)  # 向下取整
math.ceil(15.001)  # 向上取整
math.pow(2, 10)  # 求2的10次方，等同于2**10，等同于内置函数里pow(2,10)
round(4.5)  # round 内置函数而非math中的方法，实现四舍五入的功能

# 三角函数   要的是弧度，Π = 180°
print(math.sin(math.pi / 6))  # 0.49999999999999994
print(math.tan(math.pi / 3))  # 1.7320508075688767
