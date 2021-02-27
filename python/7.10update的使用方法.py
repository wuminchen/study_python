# 列表可以使用extend将列表合并
# 字典使用update合并

person1 = {'name': 'zhangsan', 'age': 18}
person2 = {'addr': 'changsha', 'height': 180}
person1.update(person2)
print(person1)

# 字典之间不支持使用加法运算
