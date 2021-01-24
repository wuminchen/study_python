# + ：可以用来拼接，用于字符串，元组，列表
print('hello' + 'nihao')
print(('good', 'world') + ('nice', 'qifei'))
print([1, 2, 3] + [7, 9, 8])

# * :可以用于字  符串元组列表，表示重复多次，不能用于字典和集合
print('hello' * 3)
print([1, 2, 3] * 3)
print((1, 2, 3, 4) * 3)

# in : 成员运算符
print('a' in 'adder')
print(1 in (1, 4, 7, 8, 5, 2, 6))
print(4 in [4, 5, 6, 8])
# in 如果用在字典中则是 用来判断key是否存在
print('addr' in {'name': 'zhangsan', 'age': 22, 'addr': 'zhongguoqingdao'})

# 带下标的遍历
nums = [19, 85, 32, 66, 47, 9]
for a in enumerate(nums):
    print(a)

# enumerate()类的作用：返回的结果是一个带有下标的列表，俗称拆包
for x, e in enumerate(nums):    # 拆包
    # e对应的就是相应下标下的元素
    print('第{}个数据是{}'.format(x, e))

# 字典中使用in方法 用的非常少，基本不用
person = {'name': 'zhangsan', 'age': 22, 'addr': 'sahndong'}
for i, k in enumerate(person):
    # k对应的就是字典中的key，而不是value
    print(i, k)