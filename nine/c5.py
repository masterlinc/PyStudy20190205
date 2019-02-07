# coding=UTF-8

# 类里面的数据变量是非常重要的特征值，不应该通过直接访问变量的方式来改变状态，正常的应该是通过方法来完成；
# 公开的 public - 可以在类的外部直接访问, 私有的 private - 在外部是无法直接读取和设置的
# python严格意义上讲是没有私有变量

class Student():

    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0

    def marking(self, score):
        self.__score = score
        if score < 0:
            print('不能打负分')
        else:
            print(self.name + '同学本次考试分数为：'+ str(self.score))
        pass

    @classmethod   # 类方法，用类来调用
    def plus_sum(cls):
        cls.sum +=1
        print(cls.sum)

    @staticmethod   # 静态方法可以用，和类以及对象没有太多关系的时候，平常不推荐静态方法
    def add(x,y):
        print('this is the static method')

studnet1 = Student('linc',18)
studnet1.marking(-2)
studnet1.__score = -1
#print(studnet1.name)
#Student.add(3,5)
#Student.plus_sum()

