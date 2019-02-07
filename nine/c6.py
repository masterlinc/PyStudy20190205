# coding=UTF-8

from c7 import Human


class Student(Human):  # People就是Student 的父类
    sum = 0


student1 = Student('linc', 20)
print(student1.sum)
result1 = student1.get_name()   # 为什么这种情况，result1 的值为none了- 因为要有return的值才行
print(student1.get_name() +'的年龄为：'+ str(student1.get_age()))



