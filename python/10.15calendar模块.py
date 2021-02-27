# calendar 日历模块
import calendar

calendar.setfirstweekday(calendar.SUNDAY)  # 设置每周的起始时间，

print(calendar.firstweekday())  # 设置每周的起始时间码，周一到周日分别对应0~6

c = calendar.calendar(2021)  # 打印某一年份的日历
print(c)

# isleap用来判断某个年份是否是闰年
print(calendar.isleap(1990))

count = calendar.leapdays(1996, 2010)  # 获取1996到2010年一共有多少个闰年  1996 2000 2004 2008
print(count)  # 4

print(calendar.month(2020, 10))  # 具体的打印某一个月份的日历
