# coding=UTF-8


class Student():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod  # @叫做装饰器
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)


student1 = Student('linc', 18)
studnet2 = Student('molly', 20 )
print(student1.name)
Student.plus_sum()
print(studnet2.name)
Student.plus_sum()
# student1.plust_sum() 不要用实例化的对象来调用类方法,直接用类来调用类方法，逻辑上才行的通；
# 如何定义一个类方法


