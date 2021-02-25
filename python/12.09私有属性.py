import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始的变量是私有变量。只能在类的内部使用

    def text(self):
        x = self.__money + 10
        return x

    def get_money(self):
        # 记录

        print(datetime.datetime.now())

        return self.__money

    def set_money(self, qian):
        if type(qian) != int:
            print('不行')
            return
        print('修改余额了。')
        self.__money = qian

    def __text(self):  # 两个下划线为开头的函数是私有函数，在外部无法调用。
        print('我是text函数')

    def text(self):  # 只能在类的内部调用私有函数。
        self.__text()


p = Person('张三', 18)

print(p.age, p.name)

#   硬调方法
p._Person__text()

# 获取私有变量的方式有：
# 1、使用对象._类名__私有变量名获取
print(p._Person__money)  #
print(p.text())

# 2、 定义方法获取
print(p.get_money())
p.set_money(100)
# 3、 使用property来获取
