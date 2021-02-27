score = float(input('请输入你的分数：'))
# 为一个 if....else 语句
if 60 > score >= 0:
    print('不及格')
elif 80 > score >= 60:
    print('一般')
elif 90 > score >= 80:
    print('良好')
elif 100 >= score >= 90:
    print('优秀')
else:
    print('不肯能的分数')
