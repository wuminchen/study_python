class Student(object):

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好，我是', self.name)


# Student（“张三”，18）
# 1.调用__new__方法,申请一个内存空间
# 2、调用__init_方法闯入参数，让self指向内存空间，填充数据
# 3、让变量s1也指向，创建好的这段内存空间

s1 = Student('张三', 18)
s1.say_hello()

# 创建一个就新的内存空间
s2 = Student('jack', 21)
s2.say_hello()
