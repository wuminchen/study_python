# 写出判断一个数是否能被 4和 6 整除的条件语句，并打印
"""num1 = int(input('请输入一个数字：'))
a = num1 % 6
b = num1 % 4
if a == 0 and b == 0 :
    print('可以被4和6整除')
else:
    print("不可以被4和6整除")"""

# 写出判断一个数能否被3或者7整除，但是不能被3和7同时整除的条件语句，并且打印
"""num2 = int(input('请继续输入一个数:'))
x = num2 % 3
y = num2 % 7
z = num2 % 21
if (x == 0 or y == 0) and (z != 0):
    print('可以被3 或者 7 整除，同时不能被3和7整除')
else:
    print('不能被3 或者7整除，或者可以同时被3和7整除。')"""

# 输入，判断输入的年份是否为闰年
"""year = int(input('输入与年份：'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print('为闰年')
else:
    print('不是闰年')"""

# 假设上课时间为15678秒，用“xx时xx分xx秒”表示出来
hour = (15678 // 60) // 60
minutes = (15678 // 60) % 60
seconds = 15678 % 60
print(str(hour) + "时" + str(minutes) + '分' + str(seconds) + '秒')
