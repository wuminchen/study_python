# sys模块：系统相关功能
import sys

print(sys.path)  # 结果是一个列表
# 表示查找模块的路径,把要导入的模块放到以下任意一个路径中都可以被找到\
# 'E:\\共享-台式\\study_python\\python',
# 'E:\\共享-台式\\study_python',
# 'C:\\Users\\chen7\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip',

sys.stdin  # 接收用户的输入，和input相关
# 可以和input函数一样，接受用户的输入，拿到的是文件的对象，和文件操作有关，暂且不讲stdin的功能比input的功能更为强大


# sys.stdout和sys.stdout默认输出在控制台
sys.stdout  # 标准输出，功能比print更强大，修改后可以改变默认输出位置，如修改到文件

sys.stdout  # 修改sys.stderr可以改变错误输出的默认位置，默认的都是在控制台打印，一旦出错，控制台就崩了，但是使用这个方法，可以将错误信息打印在某个设定的文件里，控制台就不会崩掉

sys.exit(512)
# sys.exit()   # exit是将 程序终止掉，下边的代码便不会再执行
# sys.exit()和内置函数exit()的功能一样
# 程序若正常执行，退出码应该为0
# exit(100)       # Process finished with exit code 100
# sys.exit()和内置函数exit()为程序结束后赋予一个指定的结束码
