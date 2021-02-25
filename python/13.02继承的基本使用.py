# 面向对象编程的三大特性：封装、继承、多态


# 封装：函数是对语句的封装，类是对函数和变量的封装
def test():
    a = 23
    print('hello')
    print('good')


class Person(object):
    type = 'human'  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 继承：类和类之间可以建立父子关系，子类可以使用父类属性和方法
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + '正在睡觉')


class Dog(Animal):

    def bark(self):
        print(self.name + '正在叫')


class Student(Animal):

    def study(self):
        print(self.name + '正在学习')


# Dog() 先调用__new__,再调用__init__方法
# Dog()里没有的方法会看父类，是否重写了相同的方法值，父类里也没有重写方法，查找父类的父类，直达object
#
d1 = Dog('大黄', 3)
print(d1.name)  # 父类定义的属性，子类可以直接使用
d1.sleep()  # 父类的方法，子类实例对象可以直接调用
d1.bark()

s1 = Student('小明', 18)
# 多态： 一种提高代码的灵活度的技巧
