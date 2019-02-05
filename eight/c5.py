# coding=UTF-8
#参数
# 1.必须参数
# 2，关键字参数（必须要满足必须参数，定义了多少个形参，就要传多少实参

def add(x, y):
    result = x-y
    return result

c = add(y=3, x=2)

# 增加代码的可读性

print(c)