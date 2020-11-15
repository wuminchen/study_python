# python中的for循环为for.....in循环。

# for循环的格式：for ele in iterable(可迭代的)
for i in [1, 2, 3, 4, 5]:
    print(i)

# range 内置类用来生成指定区间整数序列
# 注意 in 的后面一定是一个可迭代对象
# 可迭代对象有：字符串，列表，字典，元组，集合，range
for i in range(0, 10):  # 左闭右开
    print(i)

# 字符串
for a in "helloworld":  # 遍历字符串的每一个字母
    print(a)

# 计算1~100整数之和
result = 0
for b in range(1, 101):
    result = b + result
print(result)
