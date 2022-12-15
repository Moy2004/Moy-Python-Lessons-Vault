""""
2022 - 12 - 13 ~ 2022 - 12 - 15
جُمَادَىٰ ٱلْأُولَىٰ 19 ~   جُمَادَىٰ ٱلْأُولَىٰ 21

Health Data Saving System

before coding note:
강해 지고 있다
This project would be much easier,
if I use class and objects but since
I am doing Beginner Project,
I will use the sequence and collections

Plan
1. Make a menu where you can view / change / add the information of Patient
2. Make a collection of initial 5 patient
3. Make a functions for viewing the existing patient information (able to view one person or everyone)
4. Make a functions for changing the existing patent information (only able change one person at the time)
5. Make a functions for adding the new patient information (only add one person at the time)
6. Clean the function
"""
from pprint import pprint

# Data
# these type of dictionary are called nested dictionary
patient_data = {
    "P000": ["0-Name,1-Age,2-Height(cm),3-Residency,4-Condition,5-Treatment"],
    "P001": ["Moy", 18, 187, "Cave 1", "has a town-phobia", "move to city"],
    "P002": ["Sashko", 17, 200, "Cave 2", "brain cells loss", "move to city"],
    "P003": ["hong-hong", 18, 182, "near kim jung un", "Goes to job", "Get paid"],
    "P004": ["Monke", 5, 100, "Jungle", "Arm injury", "Physiotherapy"],
    "P005": ["Han", 18, 173, "BattleField", "Food poisoning", "Tylenol"],
}

# Main Menu
while True:
    print("\n       Patient Health Data")
    print("Action options:: ")
    print("[View   - existing]  patient data ")
    print("[Change - existing]  patient data")
    print("[Add    - incoming]  patient data")
    print("\n[Exit]\n")

    choosing = input("Enter the View/Change/Add/Exit: ").lower()
    if choosing != "view" and choosing != "change" and choosing != "add" and choosing != "exit":
        exit("Value Error: "
             "please restart and enter correct value")

    match choosing:
        case "view":
            print("\nyou have chosen to view the data")
            print("[View - ALL][View - Single]\n")

            AL_SN = input("Enter All/Single:").lower()

            if AL_SN != "all" and AL_SN != "single":
                exit("Value Error: "
                     "please restart and enter correct value")

            match AL_SN:
                case "all":
                    pprint(patient_data)

                case "single":
                    print("\nEnter the single person number "
                          "\nex.P000,P001 ... continue\n")
                    single = input("Enter the PNNN: ")
                    print(patient_data[single])

        case "change":
            print("\nYou have choose to change the patient data")
            print("Enter the single person number "
                  "\nex.P000,P001 ... \n")

            single = input("Enter the PNNN: ")

            print("")
            print(patient_data["P000"])
            print(patient_data[single])

            print("\nwhat do you want to change?\n")
            changeN = int(input("Enter the number(0~5):  "))
            changeD = input("Write  the change: ")

            patient_data[single].pop(changeN)
            patient_data[single].insert(changeN, changeD)

            print("")
            print(patient_data[single])
            print("change has been successfully made")

        case "add":
            print("\nyou have chosen to add the patient data")
            print("You will be entering... ")
            print(patient_data["P000"])
            print("")

            number = input("Give last three digit of number: ")
            numberF = "P" + number

            print("")

            if numberF not in patient_data:
                patient_data[numberF] = []
                patient_data[numberF].insert(0, input("Enter a name     :"))
                patient_data[numberF].insert(1, input("Enter a age      :"))
                patient_data[numberF].insert(2, input("Enter a height   :"))
                patient_data[numberF].insert(3, input("Enter a residency:"))
                patient_data[numberF].insert(4, input("Enter a condition:"))
                patient_data[numberF].insert(5, input("Enter a treatment:"))

            print(patient_data[numberF])

        case "exit":
            exit("Thank you for using Moy patient data system")

"""
quick 후기
ㅋㅋㅋㅋㅋ 일단 while true 후기 못 쓰는거 고침 
보기 에는 쉽지만 어느 정도 꽤 레벨이 있 었다고 본다.
시간 도 3일 2시간 즈음씩 투자 해서 만 들었다 
이제 Beginner Lesson 은 끝나고 이제 내일 부터 
Intermediate 시작 한다 헿, 이번에 끈기 있게 거의 안쉬고
프로그래밍 하니까 머리 에도 쏙쏙 들어 오고 실력도 꽤 늘고 있 는 겄같다 
Beginner 1달 만에 끝 수고 했다 ㅋㅋㅋㅋㅋ
"""       



