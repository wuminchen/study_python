# 元祖和列表很像，用来保存多个数据
# 用（）来表示一个元祖
# 元祖和列表区别在于，列表可变，元祖不可变
words = ['hello','yes', 'hi','year']
nums = (1, 9, 3, 6, 5, 6, 9, 8, 9)

# 和列表一样，也是一个有序存储数据的容器
# 可以通过下标来获取元素
print(nums[3])
# nums(3)=40 元祖是不可变类型，不能修改
print(nums.index(6))
print(nums.count(9))

# 特殊方式
ages = (18)
print(type(ages))  # 为整数类型，不是元祖
print(type(ages, ))  # 加逗号，表示元祖

# tuple 内置类
print(tuple('hello'))  # ('h', 'e', 'l', 'l', 'o')

# 元祖与列表转换
print(tuple(words)) # 列表转化为元祖
print(list(nums))   # 元祖转化为列表

print(''.join(words))

# 元祖也可以遍历
for i in nums:
    print(i)