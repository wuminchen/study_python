# in和not in 运算符
# 用来判断一个内容在可迭代对象是否存在

word = 'hello'
x = input('输')

# 判断输入的字符在字符串里是否存在
"""if word.find(x) == -1:
     print("不存在")
   else:
     print('存在')"""

"""if x in word:
    print('存在')
else:
    print('不存在')"""

if x not in word:
    print('不存在')
else:
    print("存在")