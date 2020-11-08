# 等号连接变量可以传递赋值
a = b =c = d = 'hello'
print(a,b,c,d)

m,n = 3 , 5     #拆包
print(m,n)

x = 'hello','good','yes'
print(x)    

o,*p,q = 1,2,3,4,5,6    # *表示可变长度
print(o,p,q)    #1 [2, 3, 4, 5] 6

