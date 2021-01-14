# 可变类型与不可变类型
# 不可变类型：字符串、数字、元组。 修改值，内存地址会发生变化
# 可变类型： 列表、字典、集合。   修改值，内存地址不会发生变化
# 使用内置函数 id 可以获得变量的内存地址
a = 12
b = a
print('修改前', 'a=', hex(id(a)), 'b=', hex(id(b)))
a = 10
print(b)  # 12
print('修改后', 'a=', hex(id(a)), 'b=', hex(id(b)))

nums1 = [100, 200, 300]
nums2 = nums1
print('修改前', 'nums1=', hex(id(nums1)), 'b=', hex(id(nums2)))
nums1[0] = 1
print(nums2)  # [1,200,300]
print('修改后', 'nums1=', hex(id(nums1)), 'b=', hex(id(nums2)))

