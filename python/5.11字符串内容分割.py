# split

# 字符串类型数据
x = "zhangsan-lisi-wangwu-jerry-merry-jack-tony"

m = x.split('-')  # 使用split将字符串切割成列表list
print(x)
print(m)

print(x.split('-', 2))
print(x.rsplit('-', 2))  # rsplit从右往左切开

# partition 将最前的一个指定字符串作为分隔符，分三部分
# 前 分隔符 后面
print('abcdefXmpsd'.partition('X'))

# rpartiton  将最后的一个指定字符串作为分隔符，分三部分
print('2012.12.21不要打开.mp4'.rpartition('.'))





