"""
2023 2/6 ~ 2023 2/13 (took mini break)
1444 رَجَب 15 ~ 1444 رَجَب 22

Racing

before starting project note:
In this project what I want to do is to determine
or practice the multithreading. And to do that
I am making a relay race where katakana
characters are going to race each other.
in one team there is going to be 3 katakana.
Total 3 teams.

plan:
1. Make pygame racetrack
1. Make a function for katakana racer
2. When first one work properly duplicate to three
3. Now make lock
4. Make 6 more katakana racer and assign them a lock
5. clean
"""
import time
import threading
import pygame

# making main panel for place where game will run
pygame.init()  # initialize all pygame module
play = True
main = pygame.display.set_mode((1000, 750))

# making the background
city = pygame.image.load("hande-sila-ergezer-sehir-calisma-yuzeyi-1.jpg")
city = pygame.transform.scale(city, (500, 450))

main.blit(city, (0, 0))
main.blit(city, (500, 0))

pygame.draw.rect(main, (29, 29, 27), (0, 450, 1000, 300))  # road base

pygame.draw.rect(main, (255, 142, 0), (0, 400, 1000, 10))  # yellow line
pygame.draw.rect(main, (195, 195, 195), (0, 500, 1000, 10))  # lane 2
pygame.draw.rect(main, (195, 195, 195), (0, 600, 1000, 10))  # lane 3
pygame.draw.rect(main, (195, 195, 195), (0, 700, 1000, 10))  # lane 4

# importing the cars
car_1 = pygame.image.load('2023-02-13_192042-removebg-preview.png')
car_1 = pygame.transform.scale(car_1, (100, 50))

car_2 = pygame.image.load('car2-removebg-preview.png')
car_2 = pygame.transform.scale(car_2, (120, 60))

car_3 = pygame.image.load('car3-removebg-preview.png')
car_3 = pygame.transform.scale(car_3, (150, 60))

car_4 = pygame.image.load('car4.png')
car_4 = pygame.transform.scale(car_4, (120, 60))

car_5 = pygame.image.load('car5.png')
car_5 = pygame.transform.scale(car_5, (150, 60))

# thread lock
lock_lane_1 = threading.Lock()
lock_lane_2 = threading.Lock()
lock_lane_3 = threading.Lock()


# racer group 1
def car_1_1():
    lock_lane_1.acquire()

    x = 0
    while x < 333:
        main.blit(car_1, (x, 425))
        x += 2
        time.sleep(0.05)
        pygame.display.update()

    lock_lane_1.release()


def car_1_2():
    lock_lane_1.acquire()

    x = 333
    while x < 666:
        main.blit(car_2, (x, 425))
        x += 2
        time.sleep(0.1)
        pygame.display.update()

    lock_lane_1.release()


def car_1_3():
    lock_lane_1.acquire()

    x = 666
    while x < 999:
        main.blit(car_3, (x, 425))
        x += 2
        time.sleep(0.001)
        pygame.display.update()

    lock_lane_1.release()


# racer group 2
def car_2_1():
    lock_lane_2.acquire()

    x = 0
    while x < 333:
        main.blit(car_4, (x, 525))
        x += 2
        time.sleep(0.15)
        pygame.display.update()

    lock_lane_2.release()


def car_2_2():
    lock_lane_2.acquire()

    x = 333
    while x < 666:
        main.blit(car_5, (x, 525))
        x += 2
        time.sleep(0.001)
        pygame.display.update()

    lock_lane_2.release()


def car_2_3():
    lock_lane_2.acquire()

    x = 666
    while x < 999:
        main.blit(car_2, (x, 525))
        x += 2
        time.sleep(0.0001)
        pygame.display.update()

    lock_lane_2.release()


# racer group 2
def car_3_1():
    lock_lane_3.acquire()

    x = 0
    while x < 333:
        main.blit(car_5, (x, 625))
        x += 2
        time.sleep(0.05)
        pygame.display.update()

    lock_lane_3.release()


def car_3_2():
    lock_lane_3.acquire()

    x = 333
    while x < 666:
        main.blit(car_3, (x, 625))
        x += 2
        time.sleep(0.05)
        pygame.display.update()

    lock_lane_3.release()


def car_3_3():
    lock_lane_3.acquire()

    x = 666
    while x < 999:
        main.blit(car_1, (x, 625))
        x += 2
        time.sleep(0.05)
        pygame.display.update()

    lock_lane_3.release()


# threads
c1_1 = threading.Thread(target=car_1_1)  # group 1
c1_2 = threading.Thread(target=car_1_2)
c1_3 = threading.Thread(target=car_1_3)

c2_1 = threading.Thread(target=car_2_1)  # group 2
c2_2 = threading.Thread(target=car_2_2)
c2_3 = threading.Thread(target=car_2_3)

c3_1 = threading.Thread(target=car_3_1)  # group 3
c3_2 = threading.Thread(target=car_3_2)
c3_3 = threading.Thread(target=car_3_3)


# function ofr running thread
def run():
    c1_1.start()
    c1_2.start()
    c1_3.start()

    c2_1.start()
    c2_2.start()
    c2_3.start()

    c3_1.start()
    c3_2.start()
    c3_3.start()


# initial position
def initial():
    main.blit(car_1, (0, 425))
    main.blit(car_2, (333, 425))
    main.blit(car_3, (666, 425))

    main.blit(car_4, (0, 525))
    main.blit(car_5, (333, 525))
    main.blit(car_2, (666, 525))

    main.blit(car_5, (0, 625))
    main.blit(car_3, (333, 625))
    main.blit(car_1, (666, 625))


# running pygame
while play:
    for event in pygame.event.get():
        # running the threads
        initial()
        run()
        if event.type == pygame.QUIT:
            play = False

"""
Quick 日記
Practiced multithreading and working properly
only problem I have in this project is that 
I wasn't able to erase the previously drawn car.
Didn't fix this time because it wasn't the main focus
and everything else was working, but from the next
time I will even fix this type of detail.

above all it was fun, and explored new library of
python XD. 
"""