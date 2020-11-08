# 使用bool内置类可以将其他数据类型转化为布尔值
print(bool(100))    #将100转化为布尔值
print(bool(-1))     #数字-1转化为布尔值也是True
print(bool(0))      #False


#数字里，只有0被转化为布尔值是False。其他为True

print(bool('hello'))    #True
print(bool('False'))    #True
print(bool(''))     #False
print(bool(""))     #False
#字符串中只有空字符串'',""可以转换为False,其他字符串转化为True

print(bool(None))       #False
print(bool("None"))     #Tr

print(bool([]))  #空列表为False
print(bool(()))     #空元组为False
print(bool({}))     #False

print(bool())       #False

#{}  #空字典
s = set()   #空集合
print(bool(s))

#数字0，空字符串，空列表[],空元组(),空字典{}，空集合set(),空数据None布尔值为False

#在计算机里，True和False用1和0来保存
print(True + 1)     # 2
print(False + 1)    # 1

#隐式类型转换
if 0 :
    print('hello1')  #不打印

if 1 :
    print('hello2')  #打印

if 4 > 2 :
    print('hello3')   #打印