# coding=UTF-8

def squsum(*param):
    sum = 0
    for i in param:
        sum += i*i
    print(sum)

# 可变参数，绝大部分都是用for循环来遍历可变参数中的值，然后打印出来

squsum(1,2,3,4,5,6)