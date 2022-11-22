"""
2022-11-16
1444-رَبِيع ٱلْآخِرَة-22

Functions
"""


# Function
# block of reusable code ++ algorithm

def helloworld():  # defining - name of function - (parameter):
    print("Hello World")  # work to execute


helloworld()  # calling the function


def add(x, y):
    print(x + y)


print(19, 12)


# Without knowing how many parameter will be put in

def pluscalc(*numbers):  # * means as many as in this case
    result = 0
    for number in numbers:
        result += number
    return result


print(pluscalc(10, 13, 50, 34))

"""
quick 日記
키보드 가 좋아서 프로그래밍 깔삼 해지죠
"""
