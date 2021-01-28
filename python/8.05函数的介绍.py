# 函数就是一堆准备好的代码，在需要的时候调用这一堆代码

# 代码冗余，可读性差，维护性差
"""age = int(input("年龄"))
if 0 <= age <= 3:
    for i in range(5):
        print('从前有座山')
        print('山上有座庙')
        print('庙里有个老和尚')
        print('还有一个小和尚')
        print('老和尚在给小和尚讲故事')
        print('故事的内容是')
elif 5 > age > 3:
    print('从前有座山')
    print('山上有座庙')
    print('庙里有个老和尚')
    print('还有一个小和尚')
    print('老和尚在给小和尚讲故事')
    print('故事的内容是')"""


# 把多行代码封装成一个整体（函数）
# 在python，使用关键字def来声明一个函数

# def 函数名（参数）：
#   函数要执行的操作

# 函数定义好后不会自动执行

def tel_story():
    print('从前有座山')
    print('山上有座庙')
    print('庙里有个老和尚')
    print('还有一个小和尚')
    print('老和尚在给小和尚讲故事')
    print('故事的内容是')


age = int(input("年龄"))
if 0 <= age <= 3:
    for i in range(5):
        tel_story()
elif 5 > age > 3:
    tel_story()
