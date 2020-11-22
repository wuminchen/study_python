# {} 也可以进行占位
# {}什么都不写，会读取后面的内容，一一对应
print('我是{}，今年{}岁了'.format('zhangsan', 18))

# {数字}，根据数字的顺序开始填入，从0开始
print('我是{1}，今年{0}岁了'.format('zhangsan', 18))


print('我是{name}，今年{age}岁了,我来自{addr}'.format(name='zhangsan',age= 18,addr = 'changsha'))

