# coding=UTF-8
# import sys


def add(x, y):
    result = x+y
    return result

# 形式参数，简称形参

def print1(code):
    print(code)    # 不返回任何值，这时候默认就是None

a = add(1,1000)

# 实际参数，实参

b = print1('Python hello')
print(a,b)  #
# print1('python')
#####
# Python hello
#(1001,None)
