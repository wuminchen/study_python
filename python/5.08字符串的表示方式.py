# 在python里，可以使用一对单引号，一对双引号，一对三单引号，一对三双引号表示字符串
a = 'hello'
b = "world"
c = '''123'''
d = """321"""

m = 'i said :"i am xiaoming" '
n = "I'm xiaomin"
c = """xiaomi said : "i am xiaoming" """

# 转义字符 \
# \'====>显示一个普通的单引号
# \"====>显示一个普通的双引号
# \n====>表示换行
# \t====>制表符
# \\====>显示普通的反斜线
# 在字符串前添加 r 表示原生字符
x = 'I\'m xiaoming'     # \ 对后面的字符进行转义
y = r'i/tl'
