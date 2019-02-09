# coding=UTF-8
# 数量词
# *匹配0次或者无限多次（对*前面的一个字符进行匹配）
# + 匹配一次或者无限多次
# ？ 匹配0次或者1次- 可以用来进行去重的操作

import re
a = 'pytho0python1pythonn2'

r = re.findall('n+', a)

# 贪婪 与 非贪婪(?)

print(r)
