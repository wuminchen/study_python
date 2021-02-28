# python使用 open 内置函数打开文件
# mode 默认使用rt模式打开
file = open('demo.txt', encoding='utf-8')

print(file.read())  # 所有数据读出来
file.seek(0, 0)  # 将文件指针指向文件开头

print(file.readline())  # 读取一行数据
file.seek(0, 0)

x = file.readlines()  # 将所有行的数据保存到列表里
print(x)
file.seek(0, 0)

x = file.read(30)  # 指的是读取长度
print(x)