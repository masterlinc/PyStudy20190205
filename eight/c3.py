# coding=UTF-8

def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 +10
    return damage1,damage2

damages = damage(3,6)
skill1_damages1, skill2_damages2 = damages
# 序列解包的方式去接受返回的结果,不要用元组【0~9】的方式来接受返回

print (skill1_damages1)
print (skill2_damages2)
print(type(damages))