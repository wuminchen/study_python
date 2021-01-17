person1 = {'name': 'zhangsan', 'age': 18, 'height': 180}

# 特殊在字典是以键值对的形式

# 第一种遍历方式
for x in person1:  # for in 循环获得的为key
    print(x)

# 第二种方法：获取所有的key，在遍历key，根据key在获取value
for k in person1.keys():
    print(k, '=', person1[k])

# 第三种方式：获得的value
for v in person1.values():
    print(v)

# 第四种方式
for item in person1.items():
    print(item)

for k, v in person1.items():
    print(k, v)
