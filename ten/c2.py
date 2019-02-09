# coding=UTF-8
import re
a = 'C0C++1Java2C#3Python4Javascript '

# print(a.index('Python') > -1)

result = re.findall('Python', a)


result1 = re.findall('\d', a)
# 匹配一个非数字字符。

print(result)
print(result1)
print(type(result))
