class Dog(object):
    def work(self):
        print('正在工作')


class Policedog(Dog):
    def work(self):
        print('警犬正在工作')


class Blinddog(Dog):
    def work(self):
        print('导盲犬正在工作')


class Drugdog(Dog):
    def work(self):
        print('缉毒犬正在工作')


class Person(object):
    def __init__(self, name):
        self.name = name

    def work_with_dog(self):
        self.dog.work()


p = Person('张三')

pd = Policedog()
p.dog = pd
p.work_with_dog()

bd = Blinddog()
p.dog = bd
p.work_with_dog()

dd = Policedog()
p.dog = dd
p.work_with_dog()
