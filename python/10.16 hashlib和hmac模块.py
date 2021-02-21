# hashlib和hmac模块,通常用于加密，用的还是比较多的
# hashlib模块里主要支持两个算法：md5 和 sha 加密
# 加密方式：
# 单向加密,md5/sha,只有加密的过程，没有解密的过程，
# 对称加密，
# 非对称加密rsa
import hashlib
import hmac

# 加密的内容转化为二进制
x = hashlib.md5()  # 生成一个md5对象
x.update('abc'.encode('utf8'))
print(x.hexdigest())
# 加密后的结果  abc ==> 900150983cd24fb0d6963f7d28e17f72
# 可以通过加密后的密文 倒推 回来 值是abc，但是python里目前没有一个算法来做这个事

# md5 加密不够安全了，更推荐使用 sha加密
# sha是一个系列的加密，数字不一样，得到的加密长度也不一样
h1 = hashlib.sha1('123456789'.encode('utf-8'))
print(h1.hexdigest())
# f7c3bc1d808e04732adf679965ccc34ca7ae3441

h2 = hashlib.sha224('123456789'.encode('utf-8'))  # 224位数 1个16进制占4位2进制
print(h2.hexdigest())
# 9b3e61bf29f17c75572fae2e86e17809a4513d07c8a18152acf34521

h3 = hashlib.sha384('123456789'.encode('utf-8'))
print(h3.hexdigest())
# eb455d56d2c1a69de64e832011f3393d45f3fa31d6842f21af92d2fe469c499da5e3179847334a18479c8d1dedea1be3

h4 = hashlib.sha256('123456789'.encode('utf-8'))
print(h4.hexdigest())
# 15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225

# hmac 加密可以指定密钥

