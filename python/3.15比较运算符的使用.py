# >  <  >=  <= 不等于 ！=  等等于 ==
print(2 > 1)    #True
print(2 < 4)    #True
print(4 >= 3)   #True
print(5 != 6)   #True
print('hello' == 'hello')   #True

# 比较运算符在字符串里的使用
# 字符串之间使用比较，会根据各个字符编码逐一比较
# ASCII码表
print('a' > 'b')    #False  97 > 98
print('abc' > 'b')  #False  

#数字与字符串之间只能做 == 与 ！= 比较，无法进行其他比较运算
print('a' == 90)    #False
print('a' != 97)    #True
