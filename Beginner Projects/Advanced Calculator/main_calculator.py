"""
2022 11/29 ~ 2022 12/7 = total 3 days worked
1444 -  - جُمَادَىٰ ٱلْأَوَّل ~ 1444 - 5 - جُمَادَىٰ ٱلْأَوَّل

Advance Calculator

Before Start Project Note:
This calculator will be able to do basic arithmetic + root + exponent
I know it's not as advanced but for beginner I say it is very advanced XD
Ight good luck and gameo starto

Plan:
1. make a calculator using tkinter
2. make a calculating program
3. connect the program to tkinter
"""
import math
import tkinter
import webbrowser
from tkinter import *
import tkinter.font as font

# starting the main
calculator = tkinter.Tk()
calculator.geometry('510x600')
calculator.configure(bg='#1e2124')
calculator.resizable(False, False)

# fonts
b_font = font.Font(family='Bold', size=20)  # fonts for button

# Input buttons
# still have to add values for the button
b1 = tkinter.Button(calculator, text="1", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("1"))
b2 = tkinter.Button(calculator, text="2", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("2"))
b3 = tkinter.Button(calculator, text="3", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("3"))
b4 = tkinter.Button(calculator, text="4", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("4"))
b5 = tkinter.Button(calculator, text="5", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("5"))
b6 = tkinter.Button(calculator, text="6", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("6"))
b7 = tkinter.Button(calculator, text="7", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("7"))
b8 = tkinter.Button(calculator, text="8", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("8"))
b9 = tkinter.Button(calculator, text="9", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("9"))
b0 = tkinter.Button(calculator, text="0", width=5, height=2, bg='#424549', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("0"))
bP = tkinter.Button(calculator, text="+", width=5, height=2, bg='#36393e', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("+"))
bM = tkinter.Button(calculator, text="-", width=5, height=2, bg='#36393e', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("-"))
bX = tkinter.Button(calculator, text="*", width=5, height=2, bg='#36393e', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("*"))
bD = tkinter.Button(calculator, text="/", width=5, height=2, bg='#36393e', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("/"))
bE = tkinter.Button(calculator, text="=", width=5, height=2, bg='#36393e', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda: equal())
bEx = tkinter.Button(calculator, text="^", width=5, height=2, bg='#36393e', activebackground='#282b30',
                     relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("**"))
bDt = tkinter.Button(calculator, text="○", width=5, height=2, bg='#36393e', activebackground='#282b30',
                     relief=GROOVE, fg='#faf6f6', command=lambda: panel_input("."))
bDl = tkinter.Button(calculator, text="⌫", width=5, height=2, bg='#36393e', activebackground='#282b30',
                     relief=GROOVE, fg='#faf6f6', command=lambda: panel_clear())
bB = tkinter.Button(calculator, text="ミサイル", width=11, height=2, bg='#36393e', activebackground='#282b30',
                    relief=GROOVE, fg='#faf6f6', command=lambda : missile())

# applying font / size
b1['font'] = b_font
b2['font'] = b_font
b3['font'] = b_font
b4['font'] = b_font
b5['font'] = b_font
b6['font'] = b_font
b7['font'] = b_font
b8['font'] = b_font
b9['font'] = b_font
b0['font'] = b_font
bP['font'] = b_font
bM['font'] = b_font
bX['font'] = b_font
bD['font'] = b_font
bE['font'] = b_font
bEx['font'] = b_font
bDt['font'] = b_font
bDl['font'] = b_font
bB['font'] = b_font

# Input buttons location
b1.place(x=10, y=500)
b2.place(x=110, y=500)
b3.place(x=210, y=500)
b4.place(x=10, y=400)
b5.place(x=110, y=400)
b6.place(x=210, y=400)
b7.place(x=10, y=300)
b8.place(x=110, y=300)
b9.place(x=210, y=300)
b0.place(x=310, y=500)
bP.place(x=310, y=300)
bM.place(x=410, y=300)
bX.place(x=310, y=400)
bD.place(x=410, y=400)
bE.place(x=410, y=500)
bEx.place(x=10, y=200)
bDt.place(x=110, y=200)
bDl.place(x=210, y=200)
bB.place(x=310, y=200)

# code for panel
Device_Panel = Label(calculator, bg='#36393e', height=5, width=30, fg='#faf6f6')
Device_Panel['font'] = b_font
Device_Panel.place(x=10, y=20)

# Functions for the calculation
label = ""


def panel_input(value):
    global label  # global  = scope that is outside of function (In this case we imported the label from outside)
    label += value
    Device_Panel.configure(text=label)


def panel_clear():
    global label
    label = label[:len(label) - 1]
    Device_Panel.configure(text=label)


def equal():
    global label
    result = ""
    if label != "":
        try:
            result = eval(label)
            label = ""
        except:
            result = "Beyond the level of this calculator"
            label = ""
    Device_Panel.configure(text=result)


def missile():
    webbrowser.open_new('https://www.youtube.com/watch?v=mYXjtgnTQIs&ab_channel=OkraJoe')
    calculator.destroy()


# execute
calculator.mainloop()


"""
moyの後記
중간에 학교 땜시 크게 쉬게 됬다, 다시는 학교 일 한테 타협 안 할거다.
유튜브 도움 거의 안받고 만들 어서 기분 이가 앙 기모띠 하다 
앙 기모띠 
"""
