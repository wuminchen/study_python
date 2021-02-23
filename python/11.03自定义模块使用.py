# 使用自定义模块
# 自己定义一个模块，其实就是自己写一个py文件
# 自定义模块语法有 要求，并不是随随便便 就能导入自己写的模块的
# 如果一个py文件想要当作一个模块被导入，文件名一定遵守一定的命名规范
# 有字母，数字，下划线组成，不能以数字开头

# 导入了一个模块，就能使用模块里所有的变量和函数
import my_module

print(my_module.a)
my_module.test()
print(my_module.add(1, 2))

from my_module2 import *  # 导入模块里所有的变量和函数

# 本质是读取文件里__all__属性，这个属性里定义了哪些变量和函数
# 如果模块里没有定义__all__，就会导入所有不以_开头的变量函数
# 使用from demo import *，不用写模块名字
print(m)

from my_module3 import *  # 没有设置__all__，会读取除 _ 开头的变量和函数

# _ 开头意思是建议在本模块内部使用，别的模块无法使用
print(x)
print(y)
