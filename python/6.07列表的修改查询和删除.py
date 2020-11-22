dps = ['源氏', '死神', '麦克雷', '半藏', '小美', '黑百合']
tank = ['大锤', '猩猩', '路霸', '球球', '奥丽莎']
doctor = ['天使', '安娜', '锤妹', '和尚', '莫伊拉']

# 删除数据的方法 pop remove clear
x = dps.pop()  # pop 默认删除最后一个数据，并返回这个数据。pop还可以使用index参数，删除指定下标的元素
print(x)
print(dps)  # ['源氏', '死神', '麦克雷', '半藏', '小美']

dps.remove('死神')  # 删除指定元素
# dps.remove('黑百合') 如果数据在列表中不存在，会报错
print(dps)

del dps[2]  # 尽量少用
print(dps)

dps.clear()  # 清空一个列表
print(dps)

# 查询的方法
print(doctor.index('安娜'))  # 查询元素的下标
# print(doctor.index('8d'))  会报错
print(doctor.count('天使'))  # 查询元素出现次数
# in 运算符
print('和尚' in doctor)  # True
print('8d' in doctor)   # False

# 修改元素
# 使用下标可以直接修改元素
tank[3] = '猩猩'
print(tank)
