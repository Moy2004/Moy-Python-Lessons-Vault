"""
2023 1/5
1444  جُمَادَىٰ ٱلثَّانِي 12

Recursion
"""
# recursion
# technique or method of function calling itself
# caution - If one function call itself infinitely it will have stack overflow error

"""
non-recursive way of making factorial
9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

recurvie wat to do it 
9! = 9 * 8!
"""

# non recurive way
n = 7

fact = 1

while n > 0:
    fact = fact * n
    n -= 1

print(fact)

# recursive way
n = 7

def factorial(n):
    if n < 1:
        return 1  # incase number is under 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(7))


# recursive it not always faster than iterative approach

# example using Fibonacci sequence
# Fibonacci is sum of first two numer == 0,1,1,2,3,5,8,13,21... continue

# making a function where we can find a number at certain position

# iterative way
def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

print(fibonacci(10))

# recursive way
def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)

print(fibonacci2(10))


"""
quick 日記
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
fibonacci recursive 에 100만 넣 었는데
몇 분 되어도 답 을 출력 안함
헿 이건 Intermediate 아니고 Beginner 라고 
Nuraline 형님이 그럼 그냥 가르치 는거 까 먹었데 ㅋㅋㅋ
"""

