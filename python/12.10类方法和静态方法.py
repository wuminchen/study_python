class Person(object):
    type = 'human'  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法，当用到了实例对象
    # 调用方法：
    # 1、实例对象.方法名：自动将实例对象传递给self
    # 2、类对象.方法名： 手动给self传递参数

    def eat(self, food):
        print(self.name + '吃东西' + food)

    # 类方法 如果这个函数只用到了类属性，我们可以把它定义成为一个类方法
    # 类方法会有一个参数cls,不需要手动传递参数，会自动传递对象
    # cls指的是类对象
    @classmethod
    def test(cls):
        print('test')

    # 静态方法:没有用到实例对象的任何属性，和不用类对象，可以将这个方法定义成static
    @staticmethod
    def demo():
        print('demo')


p1 = Person('张三', 18)
p2 = Person('李四', 19)

# 实例方法
p1.eat('红烧牛肉泡面')  # 会自动将对象名传递给self
# 实例对象在调用方法时，不需要给形参self传参，会自动把实例对象传递给self


Person.eat(p2, 'hotdog')  # 对象方法还可以使用类对象来调用
# 这种方式，不会自动给self传递参数，需要手动传递参数

# 静态方法
Person.demo()
p1.demo()

# 类方法：可以使用实例对象和类对象调用
p1.test()
Person.test()
