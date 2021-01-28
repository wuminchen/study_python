# def 函数名（参数）：
#      函数体
# 调用函数：函数名（参数）

# 函数声明时，我们称之为形式参数，形参的值是不固定的，只是用来占位的
# 函数调用时传入的参数，才是真正参与运算的数据，我们称之为实参`
def tel_story(place, person1, person2):
    print('从前有座山')
    print('山上有座' + place)
    print('庙里有个' + person1)
    print('还有一个' + person2)
    print(person1 + '在给' + person2 + '讲故事')
    print('故事的内容是')


# 调用函数时候传递数据
# 函数调用时候传入的参数，才是真正参与运算数据，我们称之为实参
tel_story('道馆', '老道', '道童')  # 会把实参一一对应传递，交给形参

# 通过定义变量名字给形参赋值
tel_story(place='尼姑庵', person1='师太', person2='小尼姑')



