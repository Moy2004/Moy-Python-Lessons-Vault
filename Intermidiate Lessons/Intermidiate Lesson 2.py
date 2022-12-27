"""
2022 12/27
1444  جُمَادَىٰ ٱلثَّانِي 3

Inheritance
"""

#Inheritance
# Class that is under or part of the class ex: (class animal > class dog, class cat and more)

class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Data = {self.name}, {self.age}'


class worker(person): # inheriting to the parent class

    def __init__(self, name, age, salary):
        super(worker,self).__init__(name, age) # calling the function form parent class
        self.salary = salary # because salary wasn't in person function

    def __str__(self): # this is to add the salary data to person data otherwise we cannot see salary
        text = super(worker, self).__str__()  # calling the person data
        text += f", {self.salary}"
        return text  # now salary is added to data

    def Calc_Yearly_Salary(self):
        return self.salary * 12


moy = worker('moy', 18, 80000)

print(moy)
print(moy.Calc_Yearly_Salary())

# Operator Overloading
# You can define yourself what operator will do when applied to an object
# giving extended meaning beyond their predefined operational meaning

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'{self.x}, {self.y}'

V1 = Vector(2, 3)
V2 = Vector(3, 4)

print(V1)
print(V2)

V3 = V1 + V2

print(V3)
"""
ChatGPT explanation for Operator Overloading

n Python, operator overloading allows you to define how operators such as +, -, *, /, 
and others will behave when applied to objects of a user-defined class. 
This is achieved by defining special methods in the class 
with a double underscore prefix and suffix, also known as "dunder" methods.
"""
"""
quick 日記
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
진짜 줄 46에
def __init__ 을
def __int__라 쓰고 뭘 잘못했는지 몰라서
20분 정도 날림 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
ChatGPT 가 고쳐줌 - 헿
"""



