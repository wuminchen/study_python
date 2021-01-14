import random

nums = [1, 2, [100, 201, 600, 200], 3, 6]  # 列表的嵌套
# 一个学校里，有三个办公室，有8个老师分配，完成随机分配
teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
rooms = [[], [], []]
for teacher in teachers:
    room = random.choice(rooms)  # choice 从列表里随机选择一个数据
    room.append(teacher)
print(rooms)
# 打印第0个房间人的名字
# 带下标一般使用while循环
# for 循环也可以带下标
for i, room in enumerate(rooms):
    print('房间%d里，有%d个老师' % (i, len(room)), end='')
    for teacher in room:
        print(teacher, end=' ')
    print()
