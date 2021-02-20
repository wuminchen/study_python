# all()布尔类型判断,将所有的元素都转为布尔值，然后进行判断，都是True才能为true，any()只要是true就是true
print(all(['hello', 'good', 'yes']))  # True
print(all(['hello', 0]))  # False
print(any(['hello', 'good', 'yes']))  # True
print(any(['hello', 0]))  # True

# 转换相关的bin()--将数字转换为二进制，
# chr()-将对应的字符编码转换为字符char(97)==>a
# ord()将字符转换为对应的编码
# dir()列出对象可以使用的所有方法
nums = [1, 2, 3]
print(dir(nums))
print(dir('hello'))

# divmod()-求两个数的商和余数

shang, yushu = divmod(15, 2)
print(shang, yushu)  # 7  1

# eval:执行字符串里的python代码
# exit()：退出程序
# globls(),local()
# help()--查看帮助文档
# id()获取一个数据的内存地址
# print() input()
# 判断对象相关，isinstance判断一个对象是否是由一个类创建出来
# issubclass:判断一个类是不是另一个类的子类

