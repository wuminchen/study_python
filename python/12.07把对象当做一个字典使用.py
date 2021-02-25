class Person(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __setitem__(self, key, value):
        print('__setitem__方法被被调用')
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p = Person('张三', 18, 'shanghai')
print(p.__dict__)  # 将对象转化为字典 {'name': '张三', 'age': 18}

# 不能直接把对象当做字典来使用
p['name'] = 'jack '  # 设置值 [] 语法会调用__setitem__方法
print(p.name)
print(p['name'])  # 获取值[] 使用__getitem__方法
