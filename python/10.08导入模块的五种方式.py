# 在python里，一个py文件就可以理解为一个模块
# 不是所有的py文件都可以作为模块被导入的
# 要想一个py文件能够被导入，模块的名字必须要遵守命名规则
# python为了便于程序员开发，提供了很多内置模块

# # 导入方式1：使用import + 模块名的方式进行导入（使用的最多的一个导入方式）
import time

# 导入模块以后，就可以使用这个模块里的方法和变量
print(time.time())
time.sleep(3)

# 导入方式2：导入一个模块里的方法或者变量
from random import randint  # from 模块名 import 函数名   导入一个模块里的方法或变量

print(randint(0, 2))

# 导入方式3:导入一个模块里的“所有”变量和方法
from math import *

print(pi)

# 导入方式4：导入一个模块并给这个模块起一个别名 使用的第二多的导入方式
import datetime as dt

print(dt.MAXYEAR)

# 导入方式5：from 模块名 import 函数名 as 别名
from copy import deepcopy as dp

dp(['hello', 'ni0', '54', '12'])
