class Student(object):
    __slots__ = ('name', 'age')  # 这个属性定义在类里，不在任何一个函数里，是一个元组，用来规定对象可以存在的属性

    # 说白了就是slots加一个限定，slots元组里有的属性才能用，没有的属性再使用s1.city这种方式加不进来
    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print("我的名字是{}".format(self.name))
