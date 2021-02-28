# 路径的分类
# 绝对路径：从电脑盘符开始的路径
# 相对路径：从当前文件所在的开始路径
import os

print(os.name)  #
print(os.sep)  # windows系统里，文件夹里使用\分隔
# 在非window系统里使用 | 分隔字符


# 在python里 ，\是转义字符
# 书写路径的三种方式

# 绝对路径
file1 = open('/python/demo.txt')
file2 = open(r'/python/demo.txt')
file3 = open('/python/demo.txt')

# 相对路径
file4 = open('demo.txt')
file5 = open('./bag/demo1.text')
# 用 ../ 表示上一级路径
# ./表示当前文件夹
# ./../表示上一级文件夹
# / 表示根路径
