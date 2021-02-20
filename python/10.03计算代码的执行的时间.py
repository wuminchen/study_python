import time  # 在代码运行之前，获取时间 # time 模块

start = time.time()  # 获取time模块里的time方法，可以获取当前时间的时间戳

print(start)  # 时间戳是从1970-01-01 00.00.00 UTC到现在的秒数

x = 1
for i in range(1, 98900000):
    x = x + i
print(x)

# 代码运行完成后，在获取一下时间
end = time.time()
print(end - start)
