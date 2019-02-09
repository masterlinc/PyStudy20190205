# coding=utf-8


def f1():
    a = 10

    def f2():
     #   a = 20 # 此时a是一个局部变量 ，并没有引用外部的环境变量，所以就不构成一个闭包了
        return a
    return f2


f = f1()
# print(f)
print(f.__closure__[0].cell_contents)
