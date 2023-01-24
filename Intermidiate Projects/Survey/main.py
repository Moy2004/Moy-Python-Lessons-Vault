"""
2023 1/9 ~ 2023 1/23 - see bottom note
1444 جُمَادَىٰ ٱلثَّانِيرَ 16 1444 ~ جَب 1

Survey

Before Start Project Note:
So what I want to make is, something similar to
google forms. Where you ask question and it saves it data.
And then you can view it later on as well.

Plan:
1. List questions
2. Make Tkinter main panel
3. Make function for taking survey and GUI
4. Saved data to XML
5. Make function for reviewing survey and GUI
6. Clean
"""
import customtkinter  # https://github.com/TomSchimansky/CustomTkinter/wiki/CTk-(tkinter.Tk)
import xml.dom.minidom

# starting tkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

Survey = customtkinter.CTk()

Survey.geometry("700x800")
Survey.resizable(False, True)

# XML setup
domtree = xml.dom.minidom.parse('Survey_Data.xml')
group = domtree.documentElement
domtree.writexml(open('Survey_Data.xml', 'w'))

# font
font = customtkinter.CTkFont(weight="bold", size=20)
font2 = customtkinter.CTkFont(size=15)


# function for survey
def new_survey():
    # making window and its basic feature
    new_survey = customtkinter.CTkToplevel(fg_color="#202020")
    new_survey.title("Survey")
    new_survey.geometry("700x900")
    new_survey.resizable(False, True)

    def close():
        new_survey.destroy()

    # extracting data
    def save_data():
        # reading data
        A1 = Q1_Entry.get("1.0", 'end-1c')
        A2 = Q2_Entry.get("1.0", 'end-1c')
        A3 = Q3_Entry.get("1.0", 'end-1c')
        A4 = Q4_Entry.get("1.0", 'end-1c')
        A5_1 = Q5_Turkiye.cget("text")  # could have saved all values to A5 but need to separate to append as child-node
        A5_2 = Q5_Japan.cget("text")
        A5_3 = Q5_Malaysia.cget("text")
        A5_4 = Q5_Pakistan.cget("text")
        A5 = A5_1+", "+A5_2+", "+A5_3+", "+A5_4
        A6 = Q6_Entry.get("1.0", 'end-1c')

        # Creating elements in xml file
        newPerson = domtree.createElement('Person')
        newPerson.setAttribute("id", A1)

        Ans_1 = domtree.createElement("A1")
        Ans_1.appendChild(domtree.createTextNode(A1))

        Ans_2 = domtree.createElement("A2")
        Ans_2.appendChild(domtree.createTextNode(A2))

        Ans_3 = domtree.createElement("A3")
        Ans_3.appendChild(domtree.createTextNode(A3))

        Ans_4 = domtree.createElement("A4")
        Ans_4.appendChild(domtree.createTextNode(A4))

        Ans_5 = domtree.createElement("A5")
        Ans_5.appendChild(domtree.createTextNode(A5))

        Ans_6 = domtree.createElement("A6")
        Ans_6.appendChild(domtree.createTextNode(A6))

        # append
        newPerson.appendChild(Ans_1)
        newPerson.appendChild(Ans_2)
        newPerson.appendChild(Ans_3)
        newPerson.appendChild(Ans_4)
        newPerson.appendChild(Ans_5)
        newPerson.appendChild(Ans_6)

        group.appendChild(newPerson)

        domtree.writexml(open('Survey_Data.xml', 'w'))  # confirm overwrite

        # exit the panel
        close()

    # questions
    # Q1 --------------------
    Q1_frame = customtkinter.CTkFrame(master=new_survey, width=660, height=100)
    Q1_frame.place(x=20, y=20)

    Q1_question = customtkinter.CTkLabel(master=Q1_frame, text="Q1. Name", text_color="white", font=font)
    Q1_question.place(x=20, y=20)

    Q1_Entry = customtkinter.CTkTextbox(master=Q1_frame, width=600, height=20)
    Q1_Entry.place(x=20, y=60)

    # Q2 --------------------
    Q2_frame = customtkinter.CTkFrame(master=new_survey, width=660, height=100)
    Q2_frame.place(x=20, y=140)

    Q2_question = customtkinter.CTkLabel(master=Q2_frame, text="Q2. Country of residence",
                                         text_color="white", font=font)
    Q2_question.place(x=20, y=20)

    Q2_Entry = customtkinter.CTkTextbox(master=Q2_frame, width=600, height=20)
    Q2_Entry.place(x=20, y=60)

    # Q3 --------------------
    Q3_frame = customtkinter.CTkFrame(master=new_survey, width=660, height=100)
    Q3_frame.place(x=20, y=260)

    Q3_question = customtkinter.CTkLabel(master=Q3_frame, text="Q3. Computer component that handle complex equation",
                                         text_color="white", font=font)
    Q3_question.place(x=20, y=20)

    Q3_Entry = customtkinter.CTkTextbox(master=Q3_frame, width=600, height=20)
    Q3_Entry.place(x=20, y=60)

    # Q4 --------------------
    Q4_frame = customtkinter.CTkFrame(master=new_survey, width=660, height=100)
    Q4_frame.place(x=20, y=380)

    Q4_question = customtkinter.CTkLabel(master=Q4_frame, text="Q4. What is in your pocket",
                                         text_color="white", font=font)
    Q4_question.place(x=20, y=20)

    Q4_Entry = customtkinter.CTkTextbox(master=Q4_frame, width=600, height=20)
    Q4_Entry.place(x=20, y=60)

    # Q5 --------------------
    Q5_frame = customtkinter.CTkFrame(master=new_survey, width=660, height=100)
    Q5_frame.place(x=20, y=500)

    Q5_question = customtkinter.CTkLabel(master=Q5_frame, text="Q5. Country you want to go",
                                         text_color="white", font=font)
    Q5_question.place(x=20, y=20)

    Q5_Turkiye = customtkinter.CTkCheckBox(master=Q5_frame, text="Turkiye")
    Q5_Turkiye.place(x=20, y=60)

    Q5_Japan = customtkinter.CTkCheckBox(master=Q5_frame, text="Japan")
    Q5_Japan.place(x=120, y=60)

    Q5_Malaysia = customtkinter.CTkCheckBox(master=Q5_frame, text="Malaysia")
    Q5_Malaysia.place(x=220, y=60)

    Q5_Pakistan = customtkinter.CTkCheckBox(master=Q5_frame, text="Pakistan")
    Q5_Pakistan.place(x=320, y=60)

    # Q6 --------------------
    Q6_frame = customtkinter.CTkFrame(master=new_survey, width=660, height=220)
    Q6_frame.place(x=20, y=620)

    Q6_question = customtkinter.CTkLabel(master=Q6_frame, text="Q6. Why is ice slippery",
                                         text_color="white", font=font)
    Q6_question.place(x=20, y=20)

    Q6_Entry = customtkinter.CTkTextbox(master=Q6_frame, width=600, height=140)
    Q6_Entry.place(x=20, y=60)

    # Save
    Save = customtkinter.CTkButton(master=new_survey, text="Save and Exit", command=save_data)
    Save.place(x=20, y=850)

    # Close
    Close = customtkinter.CTkButton(master=new_survey, text="Cancle", fg_color="#3B3B3B", command=close)
    Close.place(x=170, y=850)


# Main Menu
Start_Button = customtkinter.CTkButton(master=Survey, text="Start New Survey", width=600, command=new_survey)
Start_Button.pack(pady=10)


# code for viewing (connected to parsing and printing)
def view_person():
    view_person = customtkinter.CTkToplevel(fg_color="#202020")
    view_person.title("Viewing")
    view_person.geometry("700x800")
    view_person.resizable(False, True)

    # A1
    A1_frame = customtkinter.CTkFrame(master=view_person, width=660, height=100)
    A1_frame.place(x=20, y=20)

    Q1_label = customtkinter.CTkLabel(master=A1_frame, font=font2, text='Name:\n')
    Q1_label.place(x=20, y=10)

    A1_label = customtkinter.CTkLabel(master=A1_frame, font=font,
                                      text=f'{Person.getElementsByTagName("A1")[0].childNodes[0].data}')
    A1_label.place(x=20, y=30)

    # A2
    A2_frame = customtkinter.CTkFrame(master=view_person, width=660, height=100)
    A2_frame.place(x=20, y=140)

    Q2_label = customtkinter.CTkLabel(master=A2_frame, font=font2, text=f'Country:\n')
    Q2_label.place(x=20, y=10)

    A2_label = customtkinter.CTkLabel(master=A2_frame, font=font,
                                      text=f'{Person.getElementsByTagName("A2")[0].childNodes[0].data}')
    A2_label.place(x=20, y=30)

    # A3
    A3_frame = customtkinter.CTkFrame(master=view_person, width=660, height=100)
    A3_frame.place(x=20, y=260)

    Q3_label = customtkinter.CTkLabel(master=A3_frame, font=font2,
                                      text=f'Computer component that handle complex equation:\n')
    Q3_label.place(x=20, y=10)

    A3_label = customtkinter.CTkLabel(master=A3_frame, font=font,
                                      text=f'{Person.getElementsByTagName("A3")[0].childNodes[0].data}')
    A3_label.place(x=20, y=30)

    # A4
    A4_frame = customtkinter.CTkFrame(master=view_person, width=660, height=100)
    A4_frame.place(x=20, y=380)

    Q4_label = customtkinter.CTkLabel(master=A4_frame, font=font2, text=f'What is in your pocket:\n')
    Q4_label.place(x=20, y=10)

    A4_label = customtkinter.CTkLabel(master=A4_frame, font=font,
                                      text=f'{Person.getElementsByTagName("A4")[0].childNodes[0].data}')
    A4_label.place(x=20, y=30)

    # A5
    A5_frame = customtkinter.CTkFrame(master=view_person, width=660, height=100)
    A5_frame.place(x=20, y=500)

    Q5_label = customtkinter.CTkLabel(master=A5_frame, font=font2, text=f'Country you want to go to:\n')
    Q5_label.place(x=20, y=10)

    A5_label = customtkinter.CTkLabel(master=A5_frame, font=font,
                                      text=f'{Person.getElementsByTagName("A5")[0].childNodes[0].data}')
    A5_label.place(x=20, y=30)

    # A6
    A6_frame = customtkinter.CTkFrame(master=view_person, width=660, height=150)
    A6_frame.place(x=20, y=620)

    Q6_label = customtkinter.CTkLabel(master=A6_frame, font=font2, text=f'Why is ice slippery:\n')
    Q6_label.place(x=20, y=10)

    A6_label = customtkinter.CTkLabel(master=A6_frame, font=font,
                                      text=f'{Person.getElementsByTagName("A6")[0].childNodes[0].data}',
                                      wraplength=600)
    A6_label.place(x=20, y=30)


# parsing and printing
survey_data_person = group.getElementsByTagName('Person')

for Person in survey_data_person:
    if Person.hasAttribute('id'):
        person_frame = customtkinter.CTkFrame(master=Survey, width=600, height=100)
        person_frame.pack()

        padding = customtkinter.CTkFrame(master=Survey, width=600, height=20, fg_color='#242424')
        padding.pack()

        person_label = customtkinter.CTkLabel(master=person_frame, font=font,
                                              text=f'{Person.getElementsByTagName("A1")[0].childNodes[0].data}')
        person_label.place(x=20, y=35)

        person_button = customtkinter.CTkButton(master=person_frame, font=font, text="View", width=100, height=100,
                                                command=view_person)
        person_button.place(x=500, y=0)

# execute
Survey.mainloop()

"""
Quick 日記
This project only took me 4 days
But due to my final exam and other things 
I had to take a break for programming now I'm
back I will do projects and upload github projects

I leveled up a lot because of this project, 
learned how to implement the skill learned from
lesson which was saving data and manipulating
"""
