# 使用循环计算出1-100的求和结果
"""a = 0
sum1 = 0
while a < 100:
    a = a + 1
    sum1 = sum1 + a
print(sum1)"""

# 统计100以内个位是2并且能够被3整除的个数
"""a = 0
for b in range(1, 101):
    if b % 10 == 2 and b % 3 == 0:
        a = a + 1
print(a)"""

# 输入一个正整数，求它是几位数

# number = int(input('输入一个数'))
# a = 0
"""while True:
    if number % (10 ** a) != number:
        a = a + 1
    else:
        break
print(a)"""

"""a = a + 1
while True:
    number = number // 10
    if number == 0:
        break
    else:
        a = a + 1
print(a)"""

# 打印100-1000所有的水仙花数（各个位数的立方和为水仙花数本身，如153 = 1^3+5^3+3^3）
for number in range(100, 1000):
    a = number // 100
    b = (number % 100) // 10
    c = number % 10
    if number == a ** 3 + b ** 3 + c ** 3:
        print(number)
