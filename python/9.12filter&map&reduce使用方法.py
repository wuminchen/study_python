# filter 过滤,对可迭代对象，得到一个filter对象
# ，python2里是内置函数，python3里是内置类

ages = [12, 23, 30, 17, 16, 22, 19]

# filter 可定两个参数，第一个参数是函数，第二个参数是可迭代对象
# filter结果是一个filter类型的对象
x = filter(lambda ele: ele > 18, ages)
print(x)

# for a in x:
#     print(a)  # 如果不注释这一段，下面打印的为空列表

adult = list(x)
print(adult)

# map 内置类，让每一个对象执行函数里的动作
ages1 = [12, 23, 30, 17, 16, 22, 19]
m = map(lambda ele: ele + 2, ages1)
print(list(m))

# reduce以前是一个内置函数，现在是模块.函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

# 内置函数和内置类都在 builtin.py文件里，后来给放到了一个模块中
from functools import reduce

scores = [100, 89, 76, 87]

ss = reduce(lambda ele1, ele2: ele1 + ele2, scores)  # 作用类似于 (((1+2)+3)+4)+5
print(ss)

# 统计所有student的年龄加和
students = [
    {'name': 'zhangsan', 'age': 22, 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': 21, 'score': 97, 'height': 185},
    {'name': 'jack', 'age': 22, 'score': 100, 'height': 175},
    {'name': 'tony', 'age': 23, 'score': 90, 'height': 176},
    {'name': 'herry', 'age': 20, 'score': 95, 'height': 172}]

print(reduce(lambda xxx, yyy: xxx + yyy['age'], students, 0))
