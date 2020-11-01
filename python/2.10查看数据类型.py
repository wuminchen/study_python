a = 34
b = 'hello'
c = True
d = ['张三','水稻旺','收到']

#使用type内置类查看变量对应的类型
print(type(a))  #<class 'int'> 整数类型

print(type(b))  #<class 'str'> 字符串

print(type(c))  #<class 'bool'> 布尔类型

print(type(d))  #<class 'list'> 列表类型

print(type(3.14)) #<class 'float'> 浮点类型

#python里，变量没有数据类型，
#我们所说的变量的数据类型，为变量对应的值得数据类型
x = 23
print(type(x))  #<class 'int'>

x = 'hello'
print(type(x)) #<class 'str'>