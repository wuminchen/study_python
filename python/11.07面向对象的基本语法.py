# 类 是对一群具有相同特征或者行为的事务的一个统称，是抽象的，不能直接使用
# 对象是由类创建出来的一个具体的存在，可以直接使用
# 由哪一类创建出来的对象，就拥有哪一类中定义的属性和方法


# 定义类：类名怎么定义？使用class来定义一个类
# class 类名：类名一般遵守大驼峰命名法，每个单词的首字母大写
# 1、class<类名>
# 2、class<类名>（object）
class Student(object):  # 关注这个类有哪些属性和行为

    def __init__(self, name, age, height):  # 在__init__方法里，以参数的形式定义属性
        self.name = name
        self.age = age
        self.height = height

    # 行为定义一个函数
    def run(self):
        print('跑步')

    def eat(self):
        print('正在吃东西')


# 使用Student 类创建了两个实例对象s1,s2
# s1，s2都会有name、age、height属性，同时都有run和eat方法
s1 = Student('小明', 18, 1.75)    # Student()会自动调用__init__方法
s2 = Student('小美', 17, 1.65)
# 根据业务逻辑，让不同的对象执行不同行为
s1.run()
s1.eat()

s2.eat()