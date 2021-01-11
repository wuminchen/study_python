x = [100, 200, 300]
y = x  # x和y指向同一个内存空间，会相互影响
z = x.copy()  # 调用copy 方法，可以复制一个列表，这个新列表和原有列表内容一样，但指向不同的内存空间
print('0x%X,0x%X,0x%X' % (id(x), id(y), id(z)))
x[0] = 1
print(x, y, z)

# 除了使用列表自带的copy方法以外，还可以使用copy模块实现拷贝

import copy

a = copy.copy(x)  # 效果等价于x.copy 都是浅拷贝
# 深拷贝

# 切片就是一个浅拷贝
names = ['zhangsan', 'lisi', 'wangwu', 'jieke', 'chen']
names1 = names[::]
names[0] = 'candy'
print(names, names1)
