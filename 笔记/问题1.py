x = ['hello', 'good', '', '', 'what', '', 'ok', '']
i = 0
while i < len(x):
    if x[i] == '':
        x.remove(x[i])
        i = i - 1   # 去除bug ###？？？？？？  
    i = i + 1
print(x)
