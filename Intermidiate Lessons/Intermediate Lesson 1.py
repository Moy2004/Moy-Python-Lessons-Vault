"""
2022 12/26
1444  جُمَادَىٰ ٱلثَّانِي 2

Classes and Objects
"""


# objected oriented programming
# is a programming paradigm that tries to model the real world to programming

class Person:  # is a blueprint or requirements for be something
    # constructor creates the object
    def __init__(self):  # Function - Constructor/Method - Parameter(refers to object):
        self.name = "Moy"  # these are called attribute
        self.age = "18"  # from.what


First = Person()  # this will assign the variable moy and 18
print(First.name + First.age)


# usually we dont use it for this purpose because we dont want everyone to have same name and age
# so we use little different method

class Human:
    def __init__(self, Name, Age, Height):  # assigning parameter to attributes
        self.name = Name
        self.age = Age
        self.height = Height


Man_1 = Human("Moy", 18, 187)  # have to import pprint and use pprint(vars(Man_1)) to print all at once

print(Man_1.name)
print(Man_1.age)
print(Man_1.height)

Man_2 = Human("Sashko", 18, 200)  # can make infinite different ppl (just need storage XD)
Man_2.name = "Not Sashko"  # changing the value

print(Man_2.name)


# trying other Constructor/Method
# delete method

class abc:
    def __init__(self, gun):
        self.gun = gun

    def __del__(self):  # delete method
        print("gun is gone")


ak47 = abc("ak-47")
print(ak47.gun)

del ak47  # object no longer occupy the memory == gone


# traditional way to print all attributes from the object
class efg:
    def __init__(self, house, country):
        self.house = house
        self.country = country

    def __str__(self):
        return f"{self.house} {self.country}"


bobo = efg('cave1', 'usa')
print(bobo)


# class variable
# is a variable that it is independent of object but its local to class
class hij:
    amount = 0

    def __init__(self, manufacutred):
        self.car = manufacutred
        hij.amount += 1

    def __del__(self):
        hij.amount -= 1


car1 = hij("Toyota Crown")
car2 = hij("Hyundai Kona")

print(hij.amount)

"""
quick 日記
헿 이제 곧있으면
더 깔삼하고 재밌는 프로젝트
만들수 있겠다 ㅋㅋㅋㅋㅋ
"""