def add(a: int, b: int):    # 限制类型，不会报错，只会提示
    """
    这个函数将两个数字相加
    :param a: 第一个数字
    :param b: 第二个数字
    :return:两个数字相加的结果
    """
    return a + b


x = add(1, 2)
print(x)

help(add)  # 查看函数说明
