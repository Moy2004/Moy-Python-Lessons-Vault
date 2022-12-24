"""
12/19 ~ 12/24
1444 جُمَادَىٰ ٱلْأُولَىٰ 25 ~   جُمَادَىٰ ٱلْأُولَىٰ 29

Information for Specific City

before coding note:
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
지난 프로젝트 에 그게 마지막 이라 적음 ㅋㅋㅋ
이번엔 앺을 만들고 싶어서 이 프로젝트 로 선택 하게 되었다
이번 프로젝트 는 외부 도움이 많이 필요 할 거다

plan
1. Make a system parsing city info from google
2. Test if functioning using simple main menu
3. Creat a proper gui either from Tkinter or PyQt
4. Make code into an app
"""
import tkinter
import tkinter.messagebox
from tkinter import *
import tkinter.font as font

import PIL.Image
import requests
from bs4 import BeautifulSoup

from PIL import ImageTk, Image

# The Headers interface of the Fetch API allows you to perform various actions on HTTP request and response headers.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}


# Parsing-----------------------------------------------------------------------------------------------------
def information():
    location = Entry.get("1.0", "end-1c")
    location = location.replace(" ", "+")  # incase if city has space in between == New York -> New+York

    # very easy way to string format f in-front of the text
    Extract_AP = requests.get(f'https://www.google.com/search?q={location}', headers=headers)
    Extract_W = requests.get(f'https://www.google.com/search?q=weather{location}', headers=headers)
    Extract_T = requests.get(f'https://www.google.com/search?q={location}+time', headers=headers)

    parsing_AP = BeautifulSoup(Extract_AP.text, 'html.parser')
    parsing_W = BeautifulSoup(Extract_W.text, 'html.parser')
    parsing_T = BeautifulSoup(Extract_T.text, 'html.parser')

    # info desired to extract

    # I wanted to use ID to extract data sadly it didnt had ID only calss so using this method.
    # attrs is the Python package that gives you a class decorator

    Area = parsing_AP.find('div', attrs={'data-attrid': 'kc:/location/location:area'}) \
        .find('span', attrs={'class': 'LrzXr kno-fv wHYlTd z8gr9e'}).text

    try:
        Population = parsing_AP.find('div', attrs={'data-attrid': 'dc:/legacy_card'
                                                                  ':location_statistical_region_population'}) \
            .find('span', attrs={'class': 'LrzXr kno-fv wHYlTd z8gr9e'}).text
    except:
        Population = parsing_AP.find('div', attrs={'data-attrid': 'dc:/legacy_card'
                                                                  ':location_statistical_region_population'}) \
            .find('span', attrs={'class': 'LrzXr kno-fv wHYlTd z8gr9e wKYGZc'}).text  # wKYGZc caused issue

    """
     weather == Was not able to extract cause some don't provide and 
                some had local data-attrid such as JP_prefecture
     
     Time == Not all city had time next to its tab overview.
     
     So I decided to create new url and request these info from other page
    """

    Weather = parsing_W.find('span', attrs={'id': 'wob_ttm'}).text
    # wob_tm for me it was showing °C but for some reason user agent was getting imperial results
    # so me used big brain cell and change it to wob_ttm now it gives result in °C

    Time = parsing_T.find('div', attrs={'id': 'rcnt'}) \
        .find('div', attrs={'class': 'gsrt vk_bk FzvWSb YwPhnf'}).text

    return location, Area, Population, Weather, Time


# tkinter result----------------------------------------------------------------------------------------------
def print_result():
    location, Area, Population, Weather, Time = information()
    tkinter.messagebox.showinfo('result', f'The data of {location} is:\n'
                                          f'\nArea:               {Area}'
                                          f'\nPopulation:   {Population}'
                                          f'\nWeather:        {Weather}°C'
                                          f'\nTime:               {Time}')


# tkinter main------------------------------------------------------------------------------------------------

# starting tkinter
City_Searcher = tkinter.Tk()
City_Searcher.geometry("1280x720")
City_Searcher.resizable(False, False)

# font
b_font = font.Font(family='Courier', size=20)
s_font = font.Font(family='Courier', size=13)

# background image
Calling_Image = PIL.Image.open('位置情報.png')  # wanted to use jpeg but for some reason it had low quality
Background_Image = PIL.ImageTk.PhotoImage(Calling_Image)

Background = Label(City_Searcher, image=Background_Image)
Background.pack()

# City Entry
Entry = Text(City_Searcher, width=28, height=1, font=b_font, relief=FLAT)
Entry.place(x=220, y=300)

# Enter button
Enter_Button = tkinter.Button(City_Searcher, text='search', font=s_font, relief=FLAT, height=1,
                              activebackground="#adadad", command=lambda: print_result())
Enter_Button.place(x=673, y=300)

# execute-----------------------------------------------------------------------------------------------------
City_Searcher.mainloop()

"""
Quick 후기
今回のプロジェクトは
面白かった
難易度がビギナーはなかったけど
完成作を考えながら作り続けた
"""
