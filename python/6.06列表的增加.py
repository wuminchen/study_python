# 列表是用来保存多个数据的，是有序可变的
# 操作列表，一般包含增加数据，删除数据，修改数据和查询数据
# 增删改查

names = ['张三', '李四', '王五', 'jack', '张飞', '关羽', 'jerry']

# 添加元素的方法 append insert extend
names.append('黄忠')  # 在列表的最后面追加一个数据

# insert(index,object)
# index 表示下标，
# object 表示对象，具体插入哪个数据
names.insert(3, '李白')  # 在指定下标元素前插入
print(names)

x = ['王伟', '陈久', '鸣人', '无敌']
names.extend(x)  # extend(可迭代对象),将迭代对象追加到列表后面

