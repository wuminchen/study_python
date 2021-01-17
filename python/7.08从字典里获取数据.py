person = {'name': 'zhangsan', 'age': 18}

# 查找数据（字典的数据在保存时候，是无序的，不能通过下标来获取）
print(person['name'])  # 使用key获取对应的value

x = 'age'
print(person[x])

# 获取一个不存在的key时，如果key不存在，使用默认值
# 使用get方法，如果key不存在，会默认返回None,二不报错
print(person.get('height'))  # None
# 如果根据key获取不到value，使用给定值
print(person.get('gender', 'female'))  # female
print(person.get('name', 'lisi'))  # zhangsan

