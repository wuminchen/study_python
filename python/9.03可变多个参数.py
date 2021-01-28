def add_many(iter):
    x = 0
    for n in iter:
        x = x + n
    return x


nums = [1, 2, 5, 6, 3, 4, 6, 7, 2, 45]
print(add_many(nums))

# 使用input读入一个数组
numss = []
while True:
    nums = input("请输入数字，输入exit退出输入：")
    if nums == 'exit':
        break
    numss.append(int(nums))
print(numss)

x = input('请输入多个数字，数据中间使用逗号分割：')
print(x)
numsssss = x.split(',')
print(numsssss)  # ['1', '5', '6', '8', '9', '7', '4', '3', '2', '1']
