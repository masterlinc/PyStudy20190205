# coding=UTF-8
# 概括字符集

# \d \D
# \w 单词字符 \W
# \s
import re
a = 'python 1111\tjava678php\nh\rp'


r = re.findall('\s', a)
print(r)
