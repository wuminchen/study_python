import copy

# 浅复制
nums = [1, 2, 3, 4, 5]
nums1 = nums  # 赋值操作
nums2 = nums.copy()  # 浅拷贝，两个内容一模一样，但不是同一个对象
nums3 = copy.copy(nums)  # 和 nums.copy() 功能一模一样，都是浅拷贝

# 深拷贝，只能使用copy模块实现
# 浅拷贝只拷贝外层

words = ['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']
print(words)
words1 = words.copy()  # 浅拷贝
words2 = copy.deepcopy(words)  # 深拷贝
words[0] = '你好'
print(words, words1, words2)  # words1，words2不改变
words[2][0] = 1
print(words1, words2)  # words1 改变外层，内层没改    words2两层都改变
