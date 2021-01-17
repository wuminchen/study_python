words = ['a', 'c', 'x', 'f', 'q', 't', 'p', 'a', 'c', 'g', 's', 'q', 'a']
char = {}
# 统计字母次数，和最多的次数

# 第一种方法
"""for x in words:
    if x in char:
        char[x] = char[x] + 1
    else:
        char[x] = 1
print(char)"""

# 第二种方法
for x in words:
    if x not in char:
        char[x] = words.count(x)
print(char)

vs = char.values()
max_char = max(vs)
