nums = [6, 5, 3, 1, 8, 2, 4, 7]
nums.sort()  # 调用 sort 方法直接对原有的列表进行排序
print(nums)
nums.sort(reverse=True)  # reserve 参数是列表倒序排序
print(nums)

nums1 = [6, 5, 3, 1, 8, 2, 4, 7]
x = sorted(nums1)  # 内置函数sorted，会生成新的有序列表，不会改变原有的列表
print(nums1)
print(x)

names = ['zhangsan', 'lisi', 'wangwu']
names.reverse()  # reserve 方法直接将列表倒过来，不进行排序
print(names)
# 或者使用切片来倒 print(names[::-1])
