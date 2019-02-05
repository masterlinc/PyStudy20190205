# coding=UTF-8
print('a', 'b', 'c')

def demo(*param):
    print(param)
    print(type(param))

a=(1,2,3,4,5,6)
demo(*a)

# *的作用就好比解包，把元组里面的每个元素平铺拿出来传递给形参
print('!~~~~~~~~~~~~~~~~~~~~~~~~~`')

def demo1(param1, param2=2, *param):
    print(param1)
    print(param2)
    print(param)

demo('a',1,2,3)
