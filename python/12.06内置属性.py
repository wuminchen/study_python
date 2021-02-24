class Person(object):
    __slots__ = ('name', 'age')
    """
    注释 __doc__方法
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + 'eat')


# name: 张三 ，age : 18 ,eat : 函数
p1 = Person('张三', 18)
print(dir(p1))  # 列出所有支持的属性
print(p1.__class__)
print(p1.__dict__)  # 把对象属性转化成为一个字典
print(p1.__dir__())  # 等价于dir(p1)
print(p1.__doc__)  # 查看文档与注释
print(Person.__doc__)
print(p1.__module__)  # __main__模块名
print(p1.__slots__)  # 限定出现的属性
