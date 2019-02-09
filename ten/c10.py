# coding=UTF-8
# 边界匹配
# ^ 从字符串开始的位置进行匹配
# $ 从字符串结束的位置进行匹配

import re

qq = '100000'

# 4~8

r = re.findall('000$', qq)
print(r)