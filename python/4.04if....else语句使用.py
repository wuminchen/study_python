# python里的条件判断语句 if / if else / if elif else
#
# if条件判断：
#   条件成立时候，执行代码
# age = int(input('请输入你的年龄:'))    # 将input函数从字符串（str) 类型转为整数类型(int)
#
# if age < 18 :    # 字符串和数字做比较运算规则：= = 结果是False，！=结果是True，其他比较运算会报错
#     print('未满十八岁，禁止入内')
#
# if ..... else语句
# if 判断条件：
#   条件成立时执行的代码
# else
#   条件不成立时执行代码
age = int(input('请输入你的年龄:'))  # 将input函数从字符串（str) 类型转为整数类型(int)

if age < 18:                      # 字符串和数字做比较运算规则：= = 结果是False，！=结果是True，其他比较运算会报错
    print('未满十八岁，禁止入内')
else:
    print('已满十八岁，可以入内')    # if条件不满足时执行的代码
