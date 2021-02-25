class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 100

    def eat(self):
        print(self.name + '吃东西')

    def __test(self):
        print('我是Animal类里的test方法')


class Person(Animal):
    def __demo(self):
        print('我是Person私有方法')


p = Person('张三', 18)
print(p.name)

p._Person__demo()  # 无法继承父类的私有方法
p._Animal__test()  # 可以通过这种方法来调用私有方法
print(p._Animal__money)
