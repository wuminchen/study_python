# 将数据写入到内存，设计StringIO和ByteslIO两个类
from io import StringIO, BytesIO

s_io = StringIO()

s_io.write('hello')  # 将数据写入到内存里缓存起来了
s_io.write('good')

print(s_io.getvalue())

print('hello', file=open('demo.txt', 'w'))
print('good', file=s_io)  # 存到内存里了
print('yes', file=s_io)
print('ok', file=s_io)
print(s_io.getvalue())

b_io = BytesIO()
b_io.write('hello'.encode('utf8'))
print(b_io.getvalue().decode('utf8'))
