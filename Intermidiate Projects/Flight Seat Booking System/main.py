"""
2023 2/2 ~ 2023 2/3
1444 رَجَب 8 ~ 1444 رَجَب 9

Flight Booking System

Before Start Project Note:
In this project I want to determine the
skill to use object and classes, personally I wanted to build mini AI
but that is out of topic of what I have learned in this chapter.
So I will do extra unit on Machine Learning later and then do AI

plan:
1. Make a quick Ascii diagram of seats
2. Make the seats - main class
3. Make the scanner that check the availability of seat
4. Make inheritance class to input the information of a person and occupy the seat
5. Make the function that book and occupy the seats. + cannot cancel or change
6. clean
"""
import time
import sys


# declaring seat class and assigning seats
class Seat:

    def __init__(self, seat_number, availability):
        self.seat_number = seat_number
        self.availability = availability


A1 = Seat('A1', True)  # True = available, False = not available
A2 = Seat('A2', True)
A3 = Seat('A3', True)
A4 = Seat('A4', True)
A5 = Seat('A5', True)
A6 = Seat('A6', True)

All_Seats = [A1, A2, A3, A4, A5, A6]


# class for booking
class Person(Seat):

    def __init__(self, seat_number, availability, name, meal):
        super().__init__(seat_number, availability)
        self.name = name
        self.meal = meal


# scanner that check the availability of seat
def scanner():
    for x in range(6):
        if All_Seats[x].availability is True:
            time.sleep(0.5)
            print(f'Seat {x + 1} is available')


# Extra cool feature so the text is readable
def typing(void):
    msg = void
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


# booking seat option
def book_seat():
    print("""
                        .:^^~~~~~~~~~~~~^^~~~~~~~~~~~~:~~~~~~~~~~~~^^~~~~~~~~~~~~:~~~~~~~~~~~~^^~~~~~~~~~~~~:::.                           
                 .:^^^^:.?^^^^^^^^^^^!7?^^^^^^^^^^^77!^^^^^^^^^^^??^^^^^^^^^^^!77^^^^^^^^^^^??~^^^^^^^^^^!!.:^^~^.                       
            .:^^^^:.     7           :?7           ^J:           ??           :J~           7J           .7     :~~                      
        .:^^^:.          7           :?7           ~J^           ??           :J~           7J           :7       :!.                    
     .^~^:.              7  seat     :?7   seat    ~J^  seat     ??   seat    :J~  seat     7J   seat    :7        :7                    
    ^!:                  7  = A1     :?7   = A2    ~J^  = A3     ??   = A4    :J~  = A5     7J   = A6    :7         7.                   
    ^!.                  7           :?7           ~J^           ??           :J~           7J           :7         7.                   
     .^~^:.              7           :?7           ~J^           ??           :J~           7J           :7        ^!                    
        .:^^^:..         7           :?7           ~J^           ??           :J~           7J           :7       ~~                     
            ..:^^^^:.    ?           :?7           ^J^           ??           :J~           7J           .7    .^~:                      
                  .:^^^^:?!~~~~~~~~~~7!7!!!!!!!!!!!7!7!!!!!!!!!!!77!!!!!!!!!!!7!?!!!!!!!!!!!?77!!!!!!!!!!7!:^^^^.                        
                      .::^^^^^^^^^^^::::^::::::::::.::::::::::::..::::::::::::.::::::::::::..::::::::::::...
    """)
    intro_msg = "Hi, welcome to the first-class Moy Airline \n" \
                "You have payed for the ticket reserving the flight to Jakarta on 2025-7/4\n"
    typing(intro_msg)

    scanner()
    print('')

    name = input("please enter your name: ")
    seat_number = input("please enter you desired seat number[Ex, A1]: ")

    if seat_number is not [A1, A2, A3, A4, A5, A6]:
        seat_number = int(seat_number[1]) - 1
        # A1 exist, and both letter have its own index
        # A1, 1's index is 1 because start from 0.
        # and here we converted 1 to integer

        if All_Seats[seat_number].availability is False:
            print("Seat is unavailable, please book other seat")
            return

        meal = input("What meal would you like to eat: ")

        All_Seats[seat_number].availability = False
        All_Seats[seat_number] = Person(seat_number, False, name, meal)

        print("\nYour seat has been successfully reserved")
        Exit = input("Would you like to quit the system ?[y/n]: ")

        if Exit in ['y', 'Y']:
            exit("Thanks for flying with us")
        elif Exit in ['n', 'N']:
            return
        else:
            exit("bro speak no english")

    print("Seat does not exist")
    return


# viewing already existing data
def view_other():
    print("* Due to laziness of programmer number for seat is 1 lower than it is.")
    for x in range(6):
        if All_Seats[x].availability is False:
            print(vars(All_Seats[x]))
        else:
            print("There is no data for other\n")
            return


# main menu
while True:
    print("Moy Airlines\n\n"
          "1. Book flight\n"
          "2. View_Other\n"
          "3. Exit\n")
    Choice = int(input("Enter the number of your choice: "))
    if Choice not in [1, 2]:
        exit("Number of choice is not 1 or 2")

    match Choice:
        case 1:
            book_seat()
        case 2:
            view_other()
        case 3:
            exit("Thanks for Visiting moy airline")

"""
Quick 日記
쉬었다,
내 실력이 늘은거 일수도 있고 ㅋㅋ.
이번 프로젝트 에는 지난 beginner 프로젝트 에서
했던 실수들 을 고치고 더 나아가 object oriented
프로그래밍 도 어느 정도 연습 된 겄같다.
아직은 기초 지만 그래도 시작 한걸로 만족 한다.
"""
