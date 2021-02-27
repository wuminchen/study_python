nums = [6, 5, 3, 1, 8, 7, 2, 4]
j = 0
count = 0
while j < len(nums) - 1:
    i = 0
    flag = True  # 假设每一趟都没有换行
    while i < len(nums) - 1 - j:
        count = count + 1
        if nums[i] > nums[i + 1]:
            # 只要交换了，假设不成立
            flag = False
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        i = i + 1
    if flag:
        break
    j = j + 1

print(nums)
print(count)
