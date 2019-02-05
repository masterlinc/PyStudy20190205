
c = 50  # 全局变量

def add(x,y):
    c = x + y    #局部变量
    print(c)

add(1, 2 )

print(c) # 函数里面的赋值不会影响整体程序的赋值

