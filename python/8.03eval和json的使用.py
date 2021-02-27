# 内置类 list tuple set
nums = [71, 6, 54, 8, 7, 5, 3, 1, 4]
x = tuple(nums)  # 使用内置类转化为元祖
print(x)

y = set(x)  # 转化为集合
print(y)

z = list({'name': 'zhangsan', 'age': 18})
print(z)  # 为key

# python里有一个内置函数，可以执行字符串里的代码
a = 'input("请输入你的用户名")'  # a为一个字符串
b = '1+1'
eval(a)
print(eval(b))

# json的使用，把列表、元祖、字典装换为json
import json

person = {'name': 'zhangsan', 'age': 18, 'addr': 'shandong'}
# 字典把他传给前段页面，
# 先转化为'{"name": "zhangsan", "age": 18, "addr": "shandong"}'
m = json.dumps(person)  # dumps将字典、列表、集合、元祖装换为json字符串
print(m)
print(type(m))

n = '{"name":"lisi","age":18,"gender":"female"}'
p = eval(n)
print(p)
print(type(p))

s = json.loads(n)  # 将json字符串转化为python里的数据
print(s)
print(type(s))

# python       |         JSON
# True         |         true
# False        |         false
# 字符串        |         字符串
# 字典          |         对象
# 列表，元组     |         数组
print(json.dumps(['hello', 'good', 'yes', True]))
print(json.dumps(('hello', 'good', 'yes', False)))
