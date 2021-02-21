# datetime 模块
# datetime模块主要用来显示日期时间，这里主要涉及date类，用来显示日期，time类，用来显示时间
# datetime类，用来显示日期时间，timedelta类用来计算时间
import datetime as dt

# 以一个下划线 开始 _x 不能用
# 以两个下划线 开始 __x
# 以两个下划线开始,再以两个下划线结束  __x__


# 获取当前时间datetime.now()
print(dt.datetime.now())

# 创建一个日期
print(dt.date(2020, 1, 1))  # 2020-01-01

# 创建一个时间
print(dt.time(18, 23, 45))  # 18:23:45

# 计算三天之后的 日期时间
print((dt.datetime.now() + dt.timedelta(3)))

# 内置类
# list tuple int str
