class Person(object):
    type = '人类'  # 这个属性定义在类里，函数之外，我们称之为类属性。

    def __init__(self, name, age, ):
        self.name = name
        self.age = age


# Person 被称为 类对象， p1,p2 被称为 实例对象 ，对象p1,p2是通过Person类创建出来的对象
# 只要创建了一个实例对象，这个实例对象就有自己的name和age属性。
# name 和 age 是对象属性：每个实例对象都单独保存的属性。在__init__方法里，以参数形式定义
# 每个实例的对象之间的属性没有关联，互不影响。
p1 = Person('张三', 18)
p2 = Person('李四', 18)

x = p1  # x指向p1的内存地址

# 类属性可以通过类对象和实例对象获取。
print(Person.type)  # 可以通过 类对象,获取 类属性。
print(p1.type)  # 也可以通过 实例对象 获取 类属性。

# 类属性 只能通过 类对象 修改，实例对象 无法修改 类属性
p1.type = 'human'
print(p1.type)  # human
print(Person.type)  # 人类

Person.type = 'monkey'  # 修改了类属性
print(p2.type)  # monkey   没有属性，到类属性里找
print(p1.type)  # human ,已经有属性了，不会到类属性里找了。
