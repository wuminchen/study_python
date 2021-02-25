# 指定Student类继承自object
class Student(object):
    pass


# 没有指定Dog的父类，默认继承自object
class Dog:
    pass

# 新式类和景点类
# 1、新式类：继承自object的类，我们称之为新式类
# 2、经典类：不继承object类
# python2里，如果不手动指定一个父类是object
