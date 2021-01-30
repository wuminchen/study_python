def test(a):
    a = 100


def demo(nums):
    nums[0] = 10


x = 1
test(x)
print(x)  # 1

y = [1, 5, 98, 5, 6, 7, 5, 6]
demo(y)
print(y)  # [10, 5, 98, 5, 6, 7, 5, 6]
