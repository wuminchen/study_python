for number in range(2, 101):
    count = 0  # 假设这个数能被0个数字整除
    for b in range(2, number):
        if number % b == 0:
            count = count + 1
    if count == 0:
        print(number, '质数')
    else:
        print(number, '和数')
