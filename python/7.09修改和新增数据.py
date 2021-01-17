person = {'name': 'zhangsan', 'age': 18, 'addr': 'changsha'}

# 直接使用key可以修改对应的value
person['name'] = 'lisi'

# 如果key不存在，就直接在字典里添加一个新的key-value
person['gender'] = 'female'
print(person)

# pop方法，删除key-valve，结果是value
person.pop('name')
print(person)

# popitem方法,删除一个元素，结果是被删除这个元素组成的键值对
x = person.popitem()
print(person)
print(x)

del person['addr']
print(person)

# 清空一个字典
person.clear()
