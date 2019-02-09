# coding=utf-8
import json

student = [
           {'name':'qiyue', 'age':18, 'flag':False},
           {'name':'linc','age':35}
          ]
# 将编程语言中变成JSON的过程叫做 '序列化'


# NOSQL  MongoDB

json_str = json.dumps(student)
print(type(json_str))
print(json_str)