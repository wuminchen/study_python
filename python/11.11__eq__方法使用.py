class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        print('eq方法被调用')
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False


# 1,调用__new__方法申请内存空间
# 2,p1,p2内存空间不同
p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)

# is 身份运算符，比较两个对象内存地址
# == 比较两个对象的值，会调用对象的__eq__方法
# 如果__eq__方法不重写,默认比较的依然是内存地址。
print(p1 is p2)  # False
print(p1 == p2)  # False, p1调__eq__方法，self:p1,other:p2

num1 = [1, 2, 3]
num2 = [1, 2, 3]
print(num1 is num2)  # False
print(num1 == num2)  # True
list
