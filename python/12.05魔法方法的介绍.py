class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 运算符 相关方法
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):  # !=方法调用
        return 'hello'

    def __gt__(self, other):  # > 调用
        return self.age > other.age

    def __ge__(self, other):  # >=调用
        return '>='

    def __lt__(self, other):  # < 调用
        return '<'

    def __le__(self, other):  # <= 调用
        return '<= '

    def __add__(self, other):  # + 调用
        return '+'

    def __sub__(self, other):  # - 调用
        return '-'

    def __mul__(self, other):  # * 调用
        return '*'

    def __truediv__(self, other):  # / 调用
        return '/'

    def __pow__(self, power, modulo=None):  # ** 调用
        return '**'

    def __str__(self):
        return 'str'

    def __int__(self):
        return 'int'


p1 = Person('张三', 18)
p2 = Person('张三', 18)
p3 = Person('李四', 19)
print(p1 is p2)  # False

# == 运算符本质调用__eq__方法，获得__eq__方法的返回结果,没有定义就比较内存地址
print(p1 == p2)  # True

# != 方法本质调用__ne__方法，没有自定义，就__eq__方法取反
print(p1 != p2)  #
print(p1 > p3)

# 自动调用__str__方法
# 1、str()和打印对象也会调用
print(str(p1))  # 转化为字符串。默认

# 调用对象的 __int__方法
print(int(p1))
