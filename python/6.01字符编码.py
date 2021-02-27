# ASCII====>Latin1--->Unicode编码
# 字符===》数字编码

# 使用内置函数 chr 和 ord 能够查看数字和字符对应关系
print(ord('a'))  # 97 获取字符对应的数字
print(ord("撒"))
print(chr(65))  # A  获取数字对应的字母
print(ord('是'))

# 字符串转化为指定编码集 encode
# 编码集转化为字符串 decode
print("是".encode('gbk'))
print("是".encode('utf8'))
