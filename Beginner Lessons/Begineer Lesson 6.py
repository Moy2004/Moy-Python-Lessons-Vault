"""
2022-11-16
1444-رَبِيع ٱلْآخِرَة-22

Sequence and Collection
"""

# sequence
# collection of elements == assigning whole collection of value to variable

mylist = [10, 20, 30, "string", True, 4.13]  # python goodae cause can put all kind of values
print(mylist)

# index: give the information of the position that the value have
# EX. in my list the position of 10 is 0 and continue on

print(mylist[5])
print(mylist[0:3])  # : means from beginning with

# counting other way is directly -1, -2 not including 0

mylist[3] = 40  # replacing value + cannot assign new index, no [6] = x

# for loop iterate

A = [1, 2, 3, 4, 5]

for x in A:
    print(x)

# adding list onto end of other list

x = ["Hello", "this is"]
y = ["your", "Technical support"]

print(x + y)

# repeating list

x = ["Warning"]
print(x * 4)

# 3 basic function that give us information about list
x = [1, 10, 100]

print(len(x))  # len: length of index
print(max(x))  # max: return max value
print(min(x))  # min: return min value

# if = string or boolean max and min doesn't work

# Important list method
# append: adding value to the list

x = ["is", 21.422487]

x.append(39.826206)
x.insert(0, "Center")  # way to append value in to specific index

print(x)

# remove method

x.remove("Center")  # removing by specifying the value
x.pop(0)  # removing by index

print(x)

# Index method
# it will find you the index number of specified value

print(x.index(21.422487))

# sort method

x = [31, 10, 13, 44, 103]

x.sort()  # will change order of the list
# for just to see sorted ver == print(sorted(x))

print(x)

# tuple
# the value that remain the same

x = (1, 2, 3)  # is not []
# will no work if try to x[2]=10

# changing tuple == need to type cast

x = list(x)
x[2] = 10

print(x)

# dictionary
# is a sequence but doesn't have indexed it rather have KEY

person = {'name': 'sashko', 'age': '17', 'gender': 'attack helikopter'}  # {Key:Value}

person['gender'] = 'male'

print(person)  # fun part == any data type can be key
print(person.items())  # print tuple of dictionary
print(person.keys())  # print tuple of keys
print(person.values())  # print tuple value

"""
quick 日記
오늘 자유날 이라서 프로그래밍 많이 할거임 ㅋㅋㅋ
헿 이번에 공부 하니까 지속성 도 있고 나도 기분 좋 으니까 
내용이 머리속 에 쏙쏙 들 어온다 

이거 파이썬 뛰어 쓰기 좀 이상함, 잘하고 있는데 틀려다 함
그래서 지금 뛰어 쓰기 너무 많이함. 
"""


