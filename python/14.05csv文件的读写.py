import csv  # 内置模块

file = open('demo.csv', 'w', encoding='utf-8')
w = csv.writer(file)
w.writerow(['name', 'age', 'score', 'city'])
w.writerow(['zhangsan', '19', '90', '襄阳'])
w.writerow(['lisi', '19', '90', '纽约'])

w.writerows([
    ['name', 'age', 'score', 'city'],
    ['zhangsan', '19', '90', '襄阳'],
    ['lisi', '19', '90', '纽约'],
])  # 写多个列表

file1 = open('14.05-info.csv', 'r', encoding='utf8', newline='')
r = csv.reader(file1)
for data in r:
    print(data)
file.close()
