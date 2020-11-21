# 统计101-200中的质数

for number in range(101, 201):
    for b in range(2, number):      # 当for里的一直break没有被执行，就会执行else
        if number % b == 0:
            break   # 结束内循环
    else:
        print(number)
