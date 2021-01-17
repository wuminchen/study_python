persons = [{'name': "zhangsna", 'age': 18},
           {'name': 'lisi', 'age': 16},
           {'name': "wangwu", 'age': 19},
           {'name': "jialiu", 'age': 21},
           ]
# 让用户输入用户名，提示用户。如果不存在，继续输入年龄
name = input('输入你的名字')
for person in persons:
    if name == person['name']:
        print('用户名已存在')
        break
else:
    print('不存在')
    age = int(input('your ages'))
    newperson = {'name': name, 'age': age}
    persons.append(newperson)
    print(persons)
