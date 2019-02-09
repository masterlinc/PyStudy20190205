# coding=utf-8

import json


# json_str = '{"name":"qiyue","age":18}'   # json里面的字符串必须要加引号，针对name和age这种key也要加引号,jaon必须是双引号
                                         # 在Python里已经有了双引号，那么外面要表示为一个字符串，就是单引号
#JSON object array
json_str = '[{"name":"qiyue","age":18},{"name":"linc","age":35}]'

# 将JSON格式解析到编程语言对应数据结构的过程叫做'反序列化'

# 序列化的而过程

student = json.loads(json_str)
print(type(student))
print(student)
# print(student['name'])

# 对于同样的JSON字符串，不同的语言会把字符串变成不同的类型，在Python中，是转换为字典

