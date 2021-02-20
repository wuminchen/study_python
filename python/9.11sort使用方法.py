# 有几个内置函数和内置类，使用了匿名函数
nums = [4, 8, 2, 1, 7, 6]
ints = (5, 9, 2, 1, 3, 7, 4, 5)
students = [
    {'name': 'zhangsan', 'age': 22, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'herry', 'age': 20, 'score': 95, 'height': 172}
]
# 列表的sort的方法，会直接对列表进行排序


# sorted内置函数，不会改变原有函数，而是生成一个新的有序列表
x = sorted(ints)
print(x)


# 字典与字典之间不能使用比较运算，因为缺少比较规则
# 需要传递key来制定比较规则，key需要为一个函数
def foo(ele):
    return ele['age']  # 通过返回值，告诉元素按照那个属性进行排序


students.sort(key=foo)
print(students)

students.sort(key=lambda ele: ele['score'])
print(students)
