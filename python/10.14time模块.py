# time 模块

import time

print(time.time())      # 获取从1970-1-1 0.0.0 UTC（格林尼治时间）到现在的秒数
# 1604106155.9519808

print(time.strftime("%Y-%m-%d  %H:%M:%S"))  # 按照指定的格式输出时间
print(time.strftime("%y-%m-%d  %H:%M:%S"))

print(time.asctime())   # 星期几，几月，多少号，时间，年份,美国版本
# Sat Oct 31 09:02:35 2020

print(time.ctime())     # 星期几，几月，多少号，时间，年份，欧洲版本，两者差距不大，区别在于 传递的参数不一样
# Sat Oct 31 09:02:35 2020

print('hello')
time.sleep(3)       # 时间暂停3秒
print('world')