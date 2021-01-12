nums = [3, 1, 9, 8, 4, 2, 0, 7, 5]

# 第一种方法
"""nums.sort()
print(nums[-1])"""

# 第二种方法
"""x = nums[0]
for a in nums[1:]:
    if x < a:
        x = a
print(x, nums.index(x))"""

# 第三种方法
i = 0
x = nums[0]
count = 0
while i < len(nums):
    if x < nums[i]:
        x = nums[i]
        count = i
    i = i + 1
print(x, count)
