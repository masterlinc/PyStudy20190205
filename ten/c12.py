# coding=UTF-8
# 组 （）来表示
# {} 是或关系
# re 第三个参数，flag是模式的
# re.S 改变.号行为，可以匹配换行符

import re

a = 'PythonPythonC#\nPythonPython'

r = re.findall('c#.{1}', a, re.I | re.S)  # |代表且关系
print(r)