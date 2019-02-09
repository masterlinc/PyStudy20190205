# coding=UTF-8

import re
s = 'ABC3721D86'


def convert(value):
    matched = value.group()
    if int(matched) >= 6:  # 如果不加int,出现的返回值是不一样的
        return '9'
    else:
        return '0'


r = re.sub('\d', convert, s)
print(r)