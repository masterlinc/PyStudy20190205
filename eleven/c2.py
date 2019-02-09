# coding=utf-8
from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class Common():
    YELLOW = 1


#print(VIP.GREEN)  # 通过类名和下面的变量，可以直接得到返回的熟知，和教程不太一样，有可能是python版本不同造成的
#print(type(VIP.GREEN))

for v in VIP:
    print(v)