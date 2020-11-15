# 使用随机数模块 random
import random  # 导入模块

player = int(input('请输入 （’0‘ 为剪刀 ‘1’为石头 ‘2’为布）：'))
print('你输入的是', player)

computer = random.randint(0, 2)  # 生成[0,2]的随机整数
print('电脑出的是', computer)

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print('你赢了')
elif player == computer:
    print('平局')
else:
    print('你输了')
