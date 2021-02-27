class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class X(object):
    pass


class Student(Person, X):
    pass


p1 = Person('张三', 18)
p2 = Person('张三', 18)
s = Student('jack', 20)

print(p1 is p2)  # is运算符，比较两个对象的内存地址

# type(p1) 获取的是类对象
if type(p1) == Person:
    print('p1是Person类创建的实例对象')

# s这个实例对象是有Student类创建，
print(type(s) == Student)  # True
print(type(s) == Person)  # False

# isinstance ,用来判断一个对象是指定的类或者父类创建出来的
print(isinstance(s, (Student, X)))
print(isinstance(p1, Student))

# issubclass 用来判断一个类是否是另外一个类的子类
print(issubclass(Student, Person))
