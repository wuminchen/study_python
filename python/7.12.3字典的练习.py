# 将字典的key和value互换

dict1 = {'a': 100, 'b': 200, 'c': 300}

# 第一种
"""dict2 = {}
for k, v in dict1.items():
    dict2[v] = k
print(dict2)"""

# 第二种
dict2 = {v: k for k, v in dict1.items()}
print(dict2)
