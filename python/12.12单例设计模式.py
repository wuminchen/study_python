class Singleton(object):
    __instance = None  # 类属性
    __is_first = True

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  # 申请内存，创建一个对象，将对象类型设置为cls
        return cls.__instance

    def __init__(self, a, b):
        if self.__is_first:
            self.a = a
            self.b = b
            self.__is_first = False  # 增加了_is_first = False,而不是修改，要修改只能通过类对象修改


#  1,调用__new__方法调用内存
# 如果不重写__new__方法，会调用object的__new__方法
# object的__new__方法会申请内存
# 如果重写了__new__方法，需要自己手动申请内存
s1 = Singleton('呵呵', '嘿嘿嘿')
s2 = Singleton('哈哈', '嘻嘻嘻')  # 后面如何增都不会变
s3 = Singleton('嘎嘎', '嘤嘤嘤')

print(s1 is s2)
print(s1.a, s1.b)
