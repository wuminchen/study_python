# 列表推导式使用简单的语法创建一个列表
num = [i for i in range(20)]
print(num)

x = [i for i in range(30) if i % 2 == 0]
print(x)  # 偶数

y = [i for i in range(30) if i % 2]
print(y)  # 奇数

z = [(x, y) for x in range(5, 9) for y in range(10, 20)]  # z是一个列表，这个列表的元素为元祖
print(z)
