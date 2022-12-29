"""
2022 12/29
1444  جُمَادَىٰ ٱلثَّانِي 5

Synchronizing Threads
"""
# synchronizing the multiple thread that are trying to access same resource

import threading
import time # = did to see the effect otherwise milliseconds work done

# locking
# without the key(lock) the function cannot run, so it will prevent two function working on same variable
# at the same time. == the thread that is called first will acquire lock first
x = 8192

lock = threading.Lock()  # a key to start the function

def double():
    global x, lock
    lock.acquire() # it will acquire lock if it is free, if not it will wait here
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1) # tell program to wait x amount of seconds
    print("Reached the maximum")
    lock.release()

def half():
    global x
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum")
    lock.release()

t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

t1.start() # since t1 starting first we give lock to t1 first making t2 to wait
t2.start()

time.sleep(30) # just added, so it doesn't start the code below before the one above ends
# tried to use lock, but it blocks the semaphore from working, so just gave enough delay

# semaphores
# do not lock but limit the source by maximum value
# ex: allowing 5 threads at the time

semaphore = threading.BoundedSemaphore(value = 5)  # number is amount that can access the resource

def access(thread_number): # just to check which threads are getting access of the function

    print(f'{thread_number} is trying to access!')
    semaphore.acquire()  # will acquire when there is empty space

    print(f'{thread_number} was granted access!')
    time.sleep(10)

    print(f'{thread_number} is releasing')
    semaphore.release()

for thread_number in range(1, 11):
    t = threading.Thread(target= access, args=(thread_number,))
    # args is a way to pass the parameter thread_number into function access
    # args = arguments
    t.start()
    time.sleep(1)

"""
quick 日記
이걸 AI 한테 어떻게 쓸수 있을까?
흠......
먼저 AI 에 대해서 자세히 배워 야겠다
AI에 대한 지식이 있긴 하지만 프로의 비하면 
너무 얕아서 아직은 효율성 있게 어떻게 만들지 
잘 모르 겠다. 
"""

























