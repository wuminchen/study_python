# 集合是一个不重复的无序，可使用{}或set 来表示
# {} 两个意思：集合，字典
# {} 如或是键值对，为字典；如过为单一个值，就是一个集合。
person = {'name': 'zhangsan', 'age': 18}  # 字典
x = {'hello', 1, 'good'}  # 集合

names = {'zhangsan', 'lisi', 'jack', 'tony', 'jack', 'lisi'}
print(names)  # 集合自动去重，且无序


names.add('chen')  # 添加一个元素
print(names)

names.pop()  # 删除一个
print(names)

names.remove('zhangsan')  # 删除一个
print(names)

print(names.union({'胡椒粉', 'sda', 'sds'}))   # 求并集，并生成一个新的集合

names.update({'sd','奥斯卡'})  # 将一个集合拼接到当前集合
print(names)

names.clear()  # 清空一个集合
print(names)  # 空集合的表示方式为set()
