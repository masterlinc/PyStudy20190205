# coding=UTF-8

from c7 import Human


class Student(Human):  # People就是Student 的父类
                       # 子类的构造函数要继承父类的，
    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)

    sum = 0


student1 = Student('小学', 'linc', 20)
print(student1.sum)
result1 = student1.get_name()   # 为什么这种情况，result1 的值为none了- 因为要有return的值才行
print(student1.get_name() +'的年龄为：'+ str(student1.get_age()))



