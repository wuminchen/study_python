def say_hello(age, name, city="changsha"):  # 给city设定一个默认值，这种参数称为关键字参数
    print(name, age, city)


# 缺省参数


say_hello(19, 'jack')  # 有些函数的参数是，如果你传递了参数，就使用传递参数，
say_hello(18, 'sd', city='shanghai')  # 如果没有传递参数，就使用默认的值,
say_hello(city='s', age=9, name='chen')  # 也可以使用变量赋值的形式传到参数
# 如果有位置参数和关键字参数，关键字一定要放在位置参数的后边，意思就是带等号的放后边
