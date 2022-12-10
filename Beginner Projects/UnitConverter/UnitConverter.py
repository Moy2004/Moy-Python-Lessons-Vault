"""
2022 12/9 金曜日
1444 جُمَادَىٰ ٱلْأَوَّل 14

Unit Converter

Before start project note:
ミサイル作りたいww

plan
1. make a main menu
2. make a functions for converter
3. make it clean + Make function for better quality + define unacceptable values and errors)

moy quick 日記

while true 땜시 밑에 다가 일기 를 못씀ㅋㅋㅋㅋ
다음에 조심 할거 == Define what variable are allowed
이렇게 하면 굳이 하나 하나 쓸필요 없음
뭔 이야기 인지 기억 안나면 210 ~ 232 보셈

わあ、他人のコード借りずに全部私が作った。
気持ちのよさ、へっ。
"""


# Main Functions for Calculation
def temp():
    print("\nYou have chosen to convert the temperature")
    print("From = A: Celsius  B: Fahrenheit  C: Kelvin  D: Return to main \n")

    IU = input("Enter the letter: ")
    GETabcd(IU)
    if IU == "D":
        return

    IT = float(input("\nDONT WRITE UNIT\n"
                     "Enter the temperature:"))

    print("\nTo = A: Celsius  B: Fahrenheit  C: Kelvin")

    FU = input("Enter the letter: ")
    GETabcd(FU)

    print("")

    match IU, FU:
        case "A", "A":
            print(IT)
        case "A", "B":
            print(IT * 1.8 + 32)
        case "A", "C":
            print(IT + 273.15)
        case "B", "A":
            print((IT - 32) * 5 / 9)
        case "B", "B":
            print(IT)
        case "B", "C":
            print(IT + 459.67 * 5 / 9)
        case "C", "A":
            print(IT - 273.15)
        case "C", "B":
            print((IT - 273.15) * 9 / 5 + 32)
        case "C", "C":
            print(IT)


def length():
    print("\nYou have chosen to convert length")
    print("From -  A: cm  B: m  C: km  D: in  E: ft  F: yd  G: mi  H: Return to main\n")

    IU = input("Enter the letter: ")
    GETabcdefgh(IU)
    if IU == "H":
        return

    IL = float(input("\nDONT WRITE UNIT\n"
                     "Enter the length:"))

    print("To -  A: cm  B: m  C: km  D: in  E: ft  F: yd  G: mi  H: Return to main\n")

    FU = input("Enter the letter")
    GETabcdefgh(FU)

    print("")

    match IU, FU:
        case "A", "A":
            print(IL)
        case "A", "B":
            print(IL * 100)
        case "A", "C":
            print(IL * 100000)
        case "A", "D":
            print(IL / 2.54)
        case "A", "E":
            print(IL / 30.48)
        case "A", "F":
            print(IL / 91.44)
        case "A", "G":
            print(IL / 160900)
        case "B", "A":
            print(IL / 100)
        case "B", "B":
            print(IL)
        case "B", "C":
            print(IL * 1000)
        case "B", "D":
            print(IL * 39.37)
        case "B", "E":
            print(IL * 3.281)
        case "B", "F":
            print(IL * 1.094)
        case "B", "G":
            print(IL / 1609)
        case "C", "A":
            print(IL / 100000)
        case "C", "B":
            print(IL / 1000)
        case "C", "C":
            print(IL)
        case "C", "D":
            print(IL * 39370)
        case "C", "E":
            print(IL * 3281)
        case "C", "F":
            print(IL * 1094)
        case "C", "G":
            print(IL / 1.609)
        case "D", "A":
            print(IL * 2.54)
        case "D", "B":
            print(IL / 39.87)
        case "D", "C":
            print(IL / 39370)
        case "D", "D":
            print(IL)
        case "D", "E":
            print(IL / 12)
        case "D", "F":
            print(IL / 36)
        case "D", "G":
            print(IL / 63360)
        case "E", "A":
            print(IL * 30.48)
        case "E", "B":
            print(IL / 3.281)
        case "E", "C":
            print(IL / 3281)
        case "E", "D":
            print(IL * 12)
        case "E", "E":
            print(IL)
        case "E", "F":
            print(IL / 3)
        case "E", "G":
            print(IL / 5280)
        case "F", "A":
            print(IL * 91.44)
        case "F", "B":
            print(IL / 1.094)
        case "F", "C":
            print(IL / 1094)
        case "F", "D":
            print(IL * 36)
        case "F", "E":
            print(IL * 3)
        case "F", "F":
            print(IL)
        case "F", "G":
            print(IL / 1760)


def Area():
    print("\nYou have chosen to convert the Area")
    print("From = A: ㎡  B: sqft  C: pyung(평)  D: Return to main \n")

    IU = input("Enter the letter: ")
    GETabcd(IU)
    if IU == "D":
        return

    IA = float(input("\nDONT WRITE UNIT\n"
                     "Enter the Area:"))

    print("\nTo = A: ㎡  B: sqft  C: pyung(평)")

    FU = input("Enter the letter: ")
    GETabcd(FU)

    print("")

    match IU, FU:
        case "A", "A":
            print(IA)
        case "A", "B":
            print(IA * 10.7639)
        case "A", "C":
            print(IA / 3.306)
        case "B", "A":
            print(IA / 10.764)
        case "B", "B":
            print(IA)
        case "B", "C":
            print(IA / 35.583)
        case "C", "A":
            print(IA * 3.306)
        case "C", "B":
            print(IA * 35.583)
        case "C", "C":
            print(IA)


# Cleaning Functions


def GETabcd(put):
    if put.islower():
        exit("Change it to upper case")
    elif put.isdigit():
        exit("Value Error: Wrong character used")
    elif put == "A" or "B" or "C" or "D" or "E":
        return
    return


def GETabcdefgh(put):
    if put.islower():
        exit("Change it to upper case")
    elif put.isdigit():
        exit("Value Error: didnt put correct letters")
    elif put == "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H":
        return
    return


# Running the main
while True:
    print("\n-----------------------------------------------------------------")
    print("Welcome to unit converter which unit would you like to convert")
    print("A: Temperature(°C-°F-K)  B: Length(metric-imperial)  C: Area(Housing)  D: Exit\n")

    print("ONLY TYPE IN CAPITAL ALPHABET FOR ALL QUESTIONS TO FILL ")
    unit = input("Enter the letter:")
    GETabcd(unit)

    match unit:
        case "A":
            temp()
        case "B":
            length()
        case "C":
            Area()
        case "D":
            exit("Thank you for using Moy unit converter")
