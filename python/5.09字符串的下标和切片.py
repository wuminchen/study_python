# 下标又称为索引，表示第几个数据

# 可迭代对象：str list tuple dict set range 都可以遍历
# str list tuple 可通过下标来获取或操作

# 在计算机里，下标从0开始。
word = 'zhangsan'  # 字符串：一个个字符串在一起
# 可以通过下标获取或者修改指定位置数据
print(word[4])

# 字符串是不可变类型
# 对字符串的操作，都不会改变原有的字符串
# word[4] = 'x'

# 切片从字符串里复制一段指定内容，生成一个新的字符串
m = 'abcdefghijklmnopqrstuvwxyz'
print(m[5])  # m[index]====>获取指定下标的数据
# 切片语法 m[start:end:step]

print(m[2:9])  # 包含start,不包含end
print(m[2:])  # 如果只设置了start，会截取到最后
print(m[:9])  # 如果只设置了end,会从头开始，不包括结尾
print(m[3:15:2])  # step理解为间隔
print(m[3:15:1])  # step默认为1
# print(m[3:15:0])    # step不能为0
print(m[15:3:-1])  # step为负数意思为从右往左找
print(m[::])  # 从头到尾复制
print(m[::-1])  # 从尾到头复制
print(m[-9:-5])  # start和end为负数，从右边开始数
