# 多态基于继承，通过子类重写父类的方法，达到不同子类对象调用相同的父类方法，得到不同结果
# 提高代码的灵活度
class Policedog(object):
    def attack_enemy(self):
        print('正在攻击敌人')


class Blinddog(object):
    def lead_road(self):
        print('导盲犬正在领路')


class Drugdog(object):
    def search_drug(self):
        print('正在搜索')


class Person(object):
    def __init__(self, name):
        self.name = name

    def work_with_pd(self):
        self.dog.attack_enemy()

    def work_with_bd(self):
        self.dog.lead_road()

    def work_with_dd(self):
        self.dog.search_drug()


p = Person('张三')

pd = Policedog()
p.dog = pd
p.work_with_pd()

bd = Blinddog()
p.dog = bd
p.work_with_bd()
