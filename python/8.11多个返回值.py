def test(a, b):
    x = a // b
    y = a % b

    # 一般情况下，一个函数最多只会执行一个return语句
    # 特殊情况下（finally语句），一个函数可能执行多个return语句

    # return x  # 表示一个函数的结束

    # 返回多个值得方法
    # 1,return [x, y]
    # 2,return{'x'：x,'y':y}
    # 3,return(x,y)
    return x, y


result = test(13, 5)
print(result[0], result[1])
