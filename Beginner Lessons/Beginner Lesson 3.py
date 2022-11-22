"""
2022-11-11
1444-رَبِيع ٱلْآخِرَة-17

Operator and User Input
"""

# Operator
# Allows to perform action on or with the value

"""
Arithmetic Operator
+(plus), -(minus), *(multiply), /(divide)

Modulus operator
% (remainder of division),

Exponent Operator
n ** x 

Floor Division Operator
n // x (divides the value then round down to the nearest whole number)
"""
print(1 + 1)

print(10 % 3)

print(2 ** 2)

print(10 // 3)

print("\n")


"""
Assignment Operators 
=(equal), +=(add and equal), -=(minus and equal), *=(multiply and equal), /=(divide and equal), %=(remainder and equal)
"""
x = 1

x += 10
print(x)

x -= 5
print(x)

print("\n")


"""
Comparison Operator
Always give the value as a boolean 
==(equal), !=(not equal),<(Greater), >(Smaller), <=(Greater and equal), >=(Smaller and equal)
"""
x = 10
y = 20

print(x > y)

x = "앙 기모띠"
y = "앙 기모띠"

print(x == y)

print("\n")


"""
Logical Operator 
give the value as a boolean 
and(T/T), or(one have to be T), not(gives the opposite)
"""
print(10 < 20 and 20 < 30)

print(10>20 or 20<30)

print(not 10 < 20)

print("\n")

"""
membership operator
in
not in
"""

"""
identity operator 
is 
is not
"""
x = 10
if type(x) is int:
    print("x is int")
else:
    print("not int")

"""
All types
1. arithmetic operators 
2. assignment operators 
3. comparison operators 
4. logical operators 
5. identity operators 
6. membership operators 
5. boolean operators
"""

# User Input
# always stores as string - use typecast if want to specify
print("We do make exponent")
x = input("Enta whole number(base): ")
y = input("Enta whole number(exponent): ")

x = int(x)
y = int(y)

print(x**y)


"""
quick 日記
membership operator
bitwise operator
시간 남거나 궁금 하면 그냥 검색해보셈 지금 바로는 - nuraline 

오 이미 강의를 한번 마추고 다시 들 으니까 배우는 속도가 많이 빠름 ++
그때 좀 jeffery 시절 이여서 머리에 쏙쏙 다시 들어 오지도 않음 다시 배우기 시작 한거 좋은 
선택 인듯 ㅎㅎ 
"""
