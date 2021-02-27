# int 转换成整数

a = '31'
b = int(a)
print(a)
print(b)

# x = 'hello'
# y = int(x)
# # print(y)   字符串不是合法数字，会报错

x = '1a2c'
y = int(x, 16)  # 把字符串转化为16进制
print(y)
print(bin(y))

m = '12'
n = int(m, 8)
print(n)
