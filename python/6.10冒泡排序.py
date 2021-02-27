nums = [6, 5, 3, 1, 8, 7, 2, 4]

# 冒泡排序思想
# 让一个数字和它相邻的下一个数字进行比较运算
# 如果前一个数字大于后一个数字，交换两个数据位置
i = 0
while i < len(nums) - 1:
    i = i + 1
    n = 0
    while n < len(nums) - 1:
        if nums[n] > nums[n + 1]:
            nums[n], nums[n + 1] = nums[n + 1], nums[n]
        n = n + 1
    print(nums)
