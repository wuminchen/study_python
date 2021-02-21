# uuid模块 ：用来生成一个全局唯一的id模块
import uuid

# uuid1与uuid4 使用方法基本一样

# uuid1每次生成的时候都是随机的，每一次都不相同
print(uuid.uuid1())  # 32个长度，每个位置有16个选择，一共有16**32种情况

# uuid4每次生成的时候都是随机的，每一次都不相同
print(uuid.uuid4())  # uuid4使用的是最多的

# uuid3和uuid5的使用方法基本一样

# uuid3每次生成的都是固定的值，也就是说一个 zhangsan就是对应一个uuid3的值
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'zhangsan'))

# uuid5每次生成的都是固定的值，也就是说一个 zhangsan就是对应一个uuid5的值
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'zhangsan'))

# 那么这个uuid到底有啥用呢，啥时候会用到uuid呢
# 比如说我搞了一个网站，然后很多人来注册，用户留下邮箱，我给用户邮箱发邮件，邮件里有链接让用户激活
# 假设一天里有1000个人来我的网站进行注册，那我怎么来区分这1000个人呢，就是通过uuid
# 用户激活的时候链接里 包含了uuid，且每个用户的uuid都不相同，等用户再登陆的时候
# 我就可以根据uuid来判别哪个用户是哪个用户
