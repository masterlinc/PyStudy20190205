# coding=UTF-8
# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类-封装代码一系列函数，对象
# 实例化
# 类只负责定义
# 模块里只写类，对于类的实例化，调用类应该放在另外一个模块里L.
# 类和对象 究竟是什么？它们直接有什么关系？
# 类好比就是一个模板，用这个模板能够产生很多不同的对象
# 实例方法，在参数前面固定放一个self ,当调用实例方法的时候，是不需要传入self值（显胜于隐)
# 实例方法 是实例可以调用的方法，和类对象相关
# 构造函数是用来初始化特征的；


class Student(): # 类里面的参数和函数参数完全不一样
    name = '234'
    age = 0
    sum1 = 0
      # 行为 与 特征
    # '类变量' '实例变量'
    # 名字和年龄应该是

    def __init__(self, name, age):
        # 构造函数
        self.name = name
        self.age = age
        print('构造函数打印')
        print(age)
        print(name)
        print(Student.sum1)
        print(self.__class__.sum1)
        # print('student')


        #构造函数 should return none ,not ' str'
        # 构造函数，初始化对象的属性

    def do_homework(self):
        print('homework')

# class Printer()
#    def print_file(self):
#        print('name:' + self.name)  #需要self来引用变量
#        print('age: ' + str(self.age))
#        pass

# print_file() 类只负责定义，不负责运行，运行类要放在外部


student1 = Student('elwen', 18)
student2 = Student('molly', 30)
print(student1.name)
print(student2.name)
print(student1.__dict__)
print(Student.__dict__)
print(Student.name)
# print(student1.age)
# print(a)
# print(type(a))
# student2 = Student()
# student3 = Student()

# print('student1:',id(student1))
# print(id(student2))
# print(id(student3))
# student.print_file()

class StudentHomework():
    homework_name = ''