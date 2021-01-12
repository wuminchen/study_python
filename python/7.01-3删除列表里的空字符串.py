x = ['hello', 'good', '', '', 'what', '', 'ok', '']
# 第一种
"""for a in x :    # 在for....in循环时候，最好不要对列表进行增加删除操作，因为下标改变了
    if a == '':
        x.remove(a)
print(x)    # 出现bug """

# 第二种
"""i = 0
while i < len(x):
    if x[i] == '':
        x.remove(x[i])
        i = i - 1   # 去除bug ###？？？？？？  
    i = i + 1"""

# 第三种 设置一个空列表
x2 = []
for i in x:
    if i != '':
        x2.append(i)
print(x2)
