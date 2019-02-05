

def city_temp(**param):
    print(param)
    print(type(param))
    pass

city_temp(bj='32c', xm='23c', sh='31c')


print('~~~~~~~~~~~~~~~~~~~~~~~~~```')

def city_temp1(**param) :
    for key, value in param.items():
        print(key,':', value)
city_temp1(bj='32c', xm='23c', sh='31c')

# 可变参数列表