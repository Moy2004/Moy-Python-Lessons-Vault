"""
2022-11-14
1444-رَبِيع ٱلْآخِرَة-20

Loops
"""

# while loop
# loop the code until certain condition is met

x = 0

while x < 10:  # before 10
    x += 1  # do this before 10
    print(x)

# while true: == create endless loop


# for loops
# practical: make python do something over and over, Normal: To iterate sequences

for y in range(1, 11):  # last number doesn't count == count till 10
    print(y)

# Loop Control Statement
# allows controlling loop

x = 0

while x < 10:
    if x == 5:
        break  # Control Statement. Stops the loop
    x += 1
    print(x)

x = 10
while x < 20:
    x += 1
    if x == 15:
        continue  # skip one iteration
    print(x)

# extra fun
# Pass statement
# While working on code and you want to skip certain one and execute all other and to not get error use pass

x = 25

if x == 25:
    pass

print("123")

"""
quick 日記
그거 스케쥴 에 2시간 있는거 밥 땜시임 30분 밥, 헿.

"""