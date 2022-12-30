"""
2022 12/29
1444  جُمَادَىٰ ٱلثَّانِي 5

Events and Daemon Threads
"""
import threading
import time

# Event
# Thing we can trigger then react to it

event = threading.Event() #functioned to be triggered -> we can make certain thing happen

def myfunction():
    print("Waiting for event to trigger...")
    event.wait() # waiting till it triggered
    print("starting ") # this is the response to the trigger

t1 = threading.Thread(target= myfunction)
t1.start()  # before event is set function will not carry on further code

x = input("do you want to trigger the even y/n: ")

if x =='y':
    event.set() # starting the event
else:
    exit('bye')


# Daemon Thread
# They are running in the background - does not block main thread from working
# Use to read or scan something constantly

path ='text.txt' # file
text = ""  # initialized variable to contain the string/txt

def read_file(): # run constant loop - reads entire files
    global path, text

    while True:
        with open('text.txt', 'r') as f:  # opening file as read
            text = f.read() # saving the data read
        time.sleep(3) # wait 3 sec and repeat


def printloop():
    for x in range(10 ): # so it terminate
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=read_file, daemon=True)  # have to specify if it is daemon thread
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()

# can change txt while daemon thread is running, and it will prin the new edited ver

"""
quick 日記
쉽게 설명 하자면 메인 코드를 방해하지 않고 뒤에서 
계속 일하거나 대기 타고 있는거임

ex 1.
Connect to the mail server and ask how many unread messages you have.
ex 2.
Signal the GUI with the updated count.

내가 사용 생각 하기
AI 한테 무엇을 다운로드 해달라고 하면
뒤에서 AI 는 다운로드 하고 앞에서 는 
계속 이야기 를 나눈다 
"""