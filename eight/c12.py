c = 1

def func1():
    c = 2
    def func2():
       # c = 3
        print(c)
    func2()
    # print(c)
    # 链式，作用域链
func1()

print(c)