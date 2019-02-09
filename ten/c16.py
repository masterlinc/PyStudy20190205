# coding=UTF-8
# group 分组的匹配 ()

import re


S = 'life is short, i use python'

# 需要找life 和python中间的内容


r = re.search('life(.*)(py)thon', S)
print(r.group(1) +'第二组: '+ r.group(2))  # 获取分组的匹配
print(r.groups())  # 把之间的值用元组的方式反馈出来