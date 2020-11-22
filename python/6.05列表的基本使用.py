# 当我们有多个数据需要保存的时候，我们可以考虑列表
# 元素之间使用逗号进行分割
names = ['张三', '李四', '王五', 'jack', '张飞', '关羽', 'jerry']

# list(可迭代对象),将可迭代对象转化为列表
# 和字符串都可以使用下标获取元素，和对元素进行切片

names1 = list('jerry')
names2 = list(('张三', '李四', '王五', 'jack', '张飞', '关羽', 'jerry'))
print(names1)
print(names2)
print(names[2])

names[3] = '花木兰'
print(names[3])
print(names[2:5])
