# 　os模块---operationsystem操作系统
# os模块里提供的方法就是用来调用操作系统里的方法
import os

# os.name ==>获取操作系统的名字
# windows系列 ==>nt  非windows ==>posix
print(os.name)  # nt
print(os.sep)  # 路径的分隔符
# os里的path方法
print(os.path.abspath('5.01基础题目.py'))  # 获取文件的绝对路径abspath
print(os.path.isdir('10.09os模块的使用.py'))  # 用来判断一个文件是否是文件夹，是为True，否为False
print(os.path.isfile('10.09os模块的使用.py'))  # 用来判断一个文件是否是文件,文件夹不是文件
print(os.path.exists('10.09os模块的使用.py'))  # 用来判断一个文件是否存在
# 获取文件的文件名和后缀名
file_name1 = '2020.10.30.my_module2.py'
print(file_name1.rpartition('.'))
# ('2020.10.30.demo', '.', 'py')  # 得到一个元组，元组的第一个就是文件名，第二个就是分隔符，第三个就是后缀名

file_name2 = '2020.10.31.my_module2.py'
print(os.path.splitext(file_name2))  # ('2020.10.31.demo', '.py')        # 得到一个元组，元组第一个文件名，第二个为后缀名

# 其他方法
os.getwd()  # 获得当前工作目录，即当前 Python 脚本工作的目录路径。
os.listdir()  # 获取当前项目下所有的文件，包括文件和文件名
os.chdir('../')  # 切换路径（返回上一层）
os.remove('')  # 删除一个文件
os.path.getsize('name')  # 获取文件大小，以字节为单位
