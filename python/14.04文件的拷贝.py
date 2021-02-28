import os

file_name = input('输入路径')

if os.path.isfile(file_name):  # 判断是否为文件
    old_file = open(file_name, 'rb')  # 以二进制方式读取文件    # 打开旧文件，并返回文件对象

    names = os.path.splitext(file_name)  # 分隔文件名,或者使用file_name.repartition('.')
    new_file_name = names[0] + '.copy' + names[1]

    new_file = open(new_file_name, 'wb')  # 在以二进制的形式的写入

    while True:
        content = old_file.read(1024)  # 把旧文件的数据读取出来写入新文件
        new_file.write(content)
        if not content:
            break

    old_file.close()
    new_file.close()

else:
    print('不存在')

