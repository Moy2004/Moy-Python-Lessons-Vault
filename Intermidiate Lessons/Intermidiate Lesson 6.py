"""
2022 12/29
1444  جُمَادَىٰ ٱلثَّانِي 5

Queues
"""

# Queues
# Data structure very similar to list and sequences , with the difference
# they have specific order how they will get in to list or how we can access it to get out the list
# reason to use queue: when multiples thread running - need structured way to get in/out the data

import  queue


# First in first out queue

q = queue.Queue()  # declaring que
# we take out the index in the list one by one, in the order - once take out - not exist in list

numbers = [10, 20, 30, 40, 50, 60, 70]

for number in numbers:
    q.put(number)  #taking all the number from numbers and putting into que

print(q.get())  # print 10
print(q.get())  # print 20 and continue...


# Last in last our queue

q = queue.LifoQueue()

numbers = [10, 20, 30, 40, 50, 60, 70]

for x in numbers:
    q.put(x)

print(q.get())  # print 70


# Priority Queue

Q = queue.PriorityQueue()

Q.put((2, "Hellow world"))  # q.put((priority rank, what))
Q.put((11, 99))
Q.put((5, 7.5))
Q.put((1, True))

while not Q.empty():
    print(Q.get())  # prints in the priority rank first


"""
quick 日記
재밌다
오늘 할달량 그냥 넘어버림 ㅋ
"""

