# break和continue在python只能用于循环语句

# break:结束整个循环
# continue结束本轮循环开启下一个循环

"""i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i = i + 1"""

# 不断询问用户，我爱你，你爱我吗？只要答案不是爱，就一直循环，知道答案是爱。
'''a = "爱"
b = input("你爱我吗？")
while b != a:
    b = input("你爱我吗？")'''

# 不断让用户输入用户名和密码，只要用户名不是chen，密码不是123,就一直问
# 反面方法
'''username = 'chen'
password = '123'
a = input('请输入你的用户名')
b = input('请输入你的密码')
while not (a != username and b != '123'):   # 或者使用 or
    a = input('请输入你的用户名')
    b = input('请输入你的密码')'''

# 正面方法
while True:
    username = input('请输入你的用户名')
    password = input('请输入你的密码')
    if username == 'chen' and password == '123':
        break
# 正面方法更容易避免逻辑陷阱
