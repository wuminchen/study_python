# 逻辑与and运算,只有所有的运算数是True，结果才为True
4 > 3 and print('hello world')  # 输出
4 < 3 and print('你好世界')  # 不输出

# 逻辑或or运算，只有所有的算数都是False，结果才为False
4 > 3 or print('haha')  # 不输出，由于4 > 3 为 True，所以不进行
4 < 3 or print('hehe')  # 输出

# 逻辑与and 运算做取值时候，取第一个为False的值;如果都为True，取最后一个值
print(3 and 5 and 0 and 'hello')  # 0
print('good' and 'yes' and 'ok')  # ok

# 逻辑或or 运算做取值时候，取第一个为True的值;如果都为False，取最后一个值
print(0 or [] or 'Lisi' or 5 or 'ok')  # Lisi
