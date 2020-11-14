# 进制转换 将int 类型以不同进制表现出来
# 类型转换 将一个类型的数据转换成其他类型的数据
  # 如 int==>str str ==>int   bool ==>int

age = input('输入年龄：')  
# print(age + 1) 错误    #python字符串和数字做加法运算会报错
print(type(age))
new_age = int(age)  # 使用 int 内置类将其他类型转化为整数
print(type(new_age))
print(new_age + 1)

# 不同的数据类型进行运算时，运算规则不同
