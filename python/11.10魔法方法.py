# 魔法方法，也叫魔术方法，是类里的特殊的一些方法

# 1. 不需要手动调用，会在合适的时机自动调用(可以强制手动调用)
# 2. 这些方法，都是使用__开始__结束
# 3. 方法名都是使用系统规定好的，会在合适的时机自己调用

class Person(object):
    # 在创建对象时候，自动调用这个方法
    def __init__(self, name, age):
        print('init方法被调用')
        self.name = name
        self.age = age

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return '姓名:{},年龄{}'.format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        print(args, kwargs)

    def __del__(self):
        # 当对象被销毁时候，会调用这个方法
        print('del方法被调用了')


p = Person('zhangsan', 18)
# 如果不做修改，直接打印一个对象，是文件的__name__，类型，内存地址
# 当打印一个对象那个时候，会调用这个对象的__str和__repr__方法
# 如过两个方法都用了，选择__str__
print(p)
print(repr(p))
print(repr({'name': 'zhangsan', 'age': 18}))

p(1, 2, 3, x=2)

