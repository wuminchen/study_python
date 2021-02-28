# 使用python的内置函数，打开并操作一个文件

# open参数介绍
# file:打开文件的路径
# mode: 打开文件的模式，默认是 r 表示只读
# encoding：打开文件编码的方式

# open 函数会有一个返回值,返回文件
# windows系统，打开文件默认使用gbk编码打开
# 让读取和写入使用相同的编码格式
file = open('demo.txt', encoding='utf8')
print(type(file))
print(file.read())
file.close()  # 操作完了以后，关闭文件
