# 继承的特点：如果类A继承类B，那么，类A创建出的实例对象都能直接使用类B里定义的方法

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Student(Person):
    def __init__(self, name, age, school):
        # 子类在父类实现的基础上，又添加了自己的新的功能
        # 调用父类方法的两种方式
        # 1、手动调父类的方法
        # 2、 使用super
        Person.__init__(self, name, age)
        super(Student.self).__init__(name, age)
        self.school = school

    def sleep(self):
        print(self.name + '在课间睡觉')

    def study(self):
        print(self.name + '正在学习')


s = Student('jerry', 20)  # 调用了父类的__init__
s.sleep()  # 先调用自己类里的sleep方法。
print(Student.__mro__)

#
