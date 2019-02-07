class Human():
    sum = 0

    def __init__(self,name ,age ):
        self.name = name
        self.age = age
    pass

    def get_name(self):
        print(self.name)
        return self.name

    def get_age(self):
        print(self.age)
        return self.age

