# 一个列表names = ['张三', '李四', '王五', 'jack', '张飞', '关羽', 'jerry'],用户输入一个名字，就提示用户名字已经存在，没有就添加倒列表中去


"""names = ['张三', '李四', '王五', 'jack', '张飞', '关羽', 'jerry']
a = input('请输入你的用户名字')
for b in names:# 第一种方法：
    if a == b:
        print('用户名已经存在')
        break
else:
    names.append(a)
    print(names)"""

# 第二种方法
"""names = ['张三', '李四', '王五', 'jack', '张飞', '关羽', 'jerry']
a = input('请输入你的用户名字')
if a in names:
    print('用户名已经存在')
else:
    names.append(a)
    print(names)"""

# 优化冒泡排序
# 统计列表里出现次数最多的次数
# 求列表里最大数
# 删除列表里空字符串
