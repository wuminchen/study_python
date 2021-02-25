class A(object):
    def demo_a(self):
        print('我是A类里的方法demo a')


class B(object):
    def demo_b(self):
        print('我是B类里的方法demo b')


# python里允许多继承,如果有相同方法，先到先得
class C(A, B):  # 如果不写父类，默认继承object
    pass


c = C()
c.demo_a()
c.demo_b()

# 通过多个不同父类，有同名方法，可以通过查看方法，查看调用顺序（深度优先）
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
