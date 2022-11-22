"""
2022-11-18
1444-رَبِيع ٱلْآخِرَة-24

Exception Handling
"""

# Exception handling
# not all error are the same they are many type of error (ex. 4/0 == zero division error)


# try and except method
# this method exist cause normal error would have terminated the due to error but this doesn't.

try:
    x = int(input("Enter integer numerator: "))
    y = int(input("Enter integer denominator: "))
    print(x / y)
except:
    print("You didnt put integer or inputted 0 in denominator")

# specifying the error

try:
    x = int(input("enter integer: "))
    print("yes")
except ValueError:  # if value-error == print this
    print("you didnt put integer")
finally:  # will always execute no matter what happened - input thing u must do last
    print("my name is baymax")

# Exception Raising
# Incase if something went wrong, and you want to terminate you can raise the exception
# made to comment, so I can run nxt code
"""
def terminate():
    if True:
        raise Exception("앙 킹아")  # can specify the exception
    pass


terminate()
"""

# Assert method
# terminate the codes if false
x = 10
y = 20

assert (x < y)
assert (x > y)

"""
quick 日記
오늘은 방금 배운 용어좀 기록 해본다
방금 프로그래밍 쓰면서 
    while a < 100000:
    a += 1      <- 이거 잘못함 
이렇게 해버림, 여기서 잘못이 while 에 속하는 코드에 
Tab 를 안 눌름
이런 error 우리는 Indentation Error 이라고 하지 ㅎㅎ
"""
