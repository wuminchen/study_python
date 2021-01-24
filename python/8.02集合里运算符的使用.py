first = {'李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石'}
second = {'李商隐', '杜甫', '李白', '白居易', '岑参', '王昌龄'}
thrid = {'李清照', '刘禹锡', '岑参', '王昌龄', '苏轼', '王维', '李白', }

# set 支持很多运算符
# 不能使用加法
print(first - second)  # 差集
print(first & second)  # 求交集
print(first | second)  # 求并集
print(first ^ second)  # 求差集的并集，把不同的集合放在一起

