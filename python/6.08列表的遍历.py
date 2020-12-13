# 遍历：将所有的数据访问一遍。遍历针对的是可迭代对象
# while 遍历   for   in 遍历循环
dps = ['源氏', '死神', '麦克雷', '半藏', '小美', '黑百合']

# for in 循环本质调用迭代器next 方法查找下一个数据
for c in dps:
    print(c)

i = 0
while i < len(dps):
    print(dps[i])
    i = i + 1
