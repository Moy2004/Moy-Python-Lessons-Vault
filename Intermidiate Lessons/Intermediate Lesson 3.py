"""
2022 12/27
1444  جُمَادَىٰ ٱلثَّانِي 3

Multithreading
"""
# threading
# running/executing multiples codes at the same time - working same time parallel
# very useful in games when clicking two+ input/buttons at the same time

import threading  # importing module for threading

# when starting threading, start by declaring any function that u want to build

def helloworld():
    print("Hellow World")

t1 = threading.Thread(target = helloworld)  # don't () after function cause we are referring not calling
t1.start()

# trying the multi-threading
# without this method it will print function 1 then 2

def function1():
    for x in range(100):  # reason gave big number is because by the time we start the thread
        print("One")      # the code is already printed so we cannot see the effect of threading

def function2():
    for x in range(100):
        print("Two")

f1 = threading.Thread(target = function1)
f2 = threading.Thread(target = function2)

f1.start() # don't use run it will run one at the time
f2.start()

# threads will imidialtly continue to execute the code that is below the thread
# And to make the code wait until all the threads are stopped then execute -->
f1.join()
f2.join()

print("Done") # after running both f1 and f2 it will print the Done, if not do this it will print inbetween

"""
quick 日記
今日は大いに有用な知識を習いました
これからゲイムを作りな時に役に立つだろう
하지만, 게임을 만들고 싶 었으면 C# 
을 배 웠 어야지 ㅋㅋㅋㅋ
게임은 말고 앞으로 만들 AI 에  많이 도움이 될거다 
"""
