# if语句中嵌套if
# python中使用缩进来表示语句之间的结构
ticket = input('是否买票了Y/N')
if ticket == 'Y':
    print('买票了')
    safe = input('安检是否通过Y/N')
    if safe == 'Y':
        print('安检通过了，进站候车室')
    else:
        print('没通过安检，禁止进入')
else:
    print('没有买票')
