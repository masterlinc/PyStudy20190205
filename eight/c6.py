# coding=UTF-8
def print_student_files(name, age=40, gender='男', college='hust'):
    print('我叫' + name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')


print_student_files('杨凌','30', '男', '研究生')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print_student_files('果果', gender = '女')

# 形参可以有默认的参数，如果实参传递就会覆盖，如果不传递就会取默认值