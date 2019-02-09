from enum import Enum # 枚举在Python 2.7版本的时候是没有的，在3.4版本的时候才加入

class VIP(Enum):
    YELLOW = 1
    Green = 2
    BLACK = 3
    RED = 4

class Common():
    YELLOW = 1


result = VIP.Green > VIP.BLACK
result1 = VIP.Green is VIP.Green
print(result)
print(result1)
