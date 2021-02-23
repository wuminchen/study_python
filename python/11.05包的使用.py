# 包的使用
# 可以将多个具有相似或者有关联的多个模块放到一个文件夹里，便于统一管理
# 这个文件夹，就可以称之为包
# python里可以右键创建文件夹或者python包
# 文件夹和python包的区别就是  创建python包，包里会默认生成__init__文件、
# 而创建文件夹 默认不会生成这个文件
# 我们自己很少会写包，最多的是调用大佬写的包，了解就可以

from bag import recv_msg
from bag.send_msg import x
import json
import flask

print(recv_msg.y)
print(x)
