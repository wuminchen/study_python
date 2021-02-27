x = 'abcdefghijklmnskaldjasdas'

# 获取字符串的长度，使用len函数
print(len(x))

# 查找内容的相关方法 find/index/rfind/rindex,获取指定字符的下标
print(x.find('l'))
print(x.index('l'))

print(x.find('z'))  # 如果不存在，结果为-1
# print(x.index('z')) 如果不存在，报错
print(x.rfind('l'))  # 最大的下标
print(x.rindex('l'))

# is开头的是判断，结果为布尔类型
print('hello'.startswith('h'))  # True 判断开头
print('hello'.endswith('o'))  # True 判断结尾
print('hello'.isalpha())  # 判断字符串是否为字母
print('1235'.isdigit())  # 判断字符串是否为数字
print('sda15'.isalnum())  # 判断是否由数字或者字母组成，不能有其他符号如+ - * /
print('       '.isspace())  # 判断是否全部由空格组成

# replace 用来替换字符串
word = 'hello'
m = word.replace('l', 'x')  # 将字符串里的所有l 替换成x
print(word)  # hello 字符串不可改变！！！！
print(m)  # hexxo 原字符串不会改变，要用新的字符串承接替换后的结果

#
