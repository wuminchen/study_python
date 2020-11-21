# 2 -100的素数

for number in range(2, 101):
    flag = True     # 每次假设number都为素数
    for b in range(2, number):
        if number % b == 0:  # 除尽了，为合数
            flag = False
            break
    if flag:    # if flag == True
        print(number)