# random模块用来生成一个随机的数字
import random

# 生成[2,9]之间的整数，包括2也包括9
print(random.randint(2, 9))

# 生成0-1之间的随机浮点数,包含0但是不包含1   [0,1)
print(random.random())

# randrange(a,b)  生成[a,b)之间的随机整数
print(random.randrange(2, 9))

# choice 用来在列表里或者可迭代对象里随机抽取一个数据
print(random.choice(['zhangsan', 'lisi', 'jack', 'herry', 'huamulan', 'sunwukong']))

# sample 用来在可迭代对象里随机抽取n个数据
print(random.sample(['zhangsan', 'lisi', 'jack', 'herry', 'huamulan', 'sunwukong'], 2))
