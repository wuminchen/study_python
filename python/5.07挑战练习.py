# 用for循环写九九乘法表
"""for l in range(1, 10):
    for n in range(1, l + 1):
        print(l, '*', n, '=', (l * n), sep='', end='\t')yi
    print()"""

# "百马百担"问题：一匹大马能驮3担货，一匹中马能驮2担货，两匹小马能驮1担货，如果用一百匹马驮一百担货，问有大、中、小马各几匹？
for b in range(0, 34):
    for m in range(0, 51):
        if 3 * b + 2 * m + (100 - m - b) * 0.5 == 100:
            print(b, m, 100 - b - m)
