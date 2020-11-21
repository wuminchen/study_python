# 求斐波那契数列第n个数字
# 斐波那契数列：1，1，2，3，5，8，13......

i = int(input('第n个'))

num1 = 1
num2 = 1
for n in range(0, i-2):
    a = num1
    num1 = num2
    num2 = a + num2
print(num2)
