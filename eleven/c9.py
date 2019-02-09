# coding=utf-8
# 闭包是由函数及定义的外部环境变量构成的一个整体

def curve_pre():
    a = 25     # a 的局部变量在curve的外面  a 为环境变量

    def curve(x):
        return a*x*x
    return curve  # 函数可以作为一个返回值


a = 10
r = curve_pre()

print(r.__closure__)
print(r.__closure__[0].cell_contents)

print(r(2))