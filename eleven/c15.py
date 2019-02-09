# coding=utf-8

# 解决旅行者的当前所在位置

orgin = 0

def factory(pos):

    def go(step):
    #    nonlocal pos # 在Python2.7中没有nonlocal的定义
        new_post = pos + step
        pos = new_post
        return new_post
    return go


r = factory(orgin)
print(r(3))
print(r(5))
print(r(3))
