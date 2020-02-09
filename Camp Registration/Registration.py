import tkinter
from tkinter import *
#creating screen
page = tkinter.Tk()
#naming screen
page.title('Camp Sign-up')
#setting screen size
page.geometry("1000x500")
#creating text
Title = tkinter.Label(page, text='Registration', font=('arial') ).pack()

FullName = tkinter.Label(page, text='Full Name:', font=('arial')).place(x=110, y=50)
#creating entry data
fullname=StringVar()

FullNameValue = Entry(page, textvariable=fullname, width=25,).place(x=200, y=53)



Adress = tkinter.Label(page, text='Adress:', font=('arial')).place(x=130, y=102)

adress=StringVar()

AdressValue = Entry(page, textvariable=adress, width=25,).place(x=200, y=106)



ParentialFigure = tkinter.Label(page, text='Parent Or Gaurdian:', font=('arial')).place(x=45, y=150)

parent=StringVar()

ParentValue = Entry(page, textvariable=parent, width=25,).place(x=200, y=153)



Age = tkinter.Label(page, text='Age:', font=('arial')).place(x=150, y=200)

age=StringVar()

AgeValue = Entry(page, textvariable=age, width=25,).place(x=200, y=203)


#second pannel


HomeChurch = tkinter.Label(page, text='	Home Church:', font=('arial')).place(x=310, y=50)

homechurch=StringVar()

HomeChurchValue = Entry(page, textvariable=homechurch, width=25,).place(x=500, y=53)



InsuranceCo = tkinter.Label(page, text='InsuranceCo:', font=('arial')).place(x=390, y=102)

insuracecomp=StringVar()

InsuranceCoValue = Entry(page, textvariable=insuracecomp, width=25,).place(x=500, y=106)



PolicyNumber = tkinter.Label(page, text='Policy Number:', font=('arial')).place(x=375, y=150)

policynumber=StringVar()

PolicyNumberValue = Entry(page, textvariable=policynumber, width=25,).place(x=500, y=153)



ContactNumber = tkinter.Label(page, text='Contact Number:', font=('arial')).place(x=367, y=200)

contactnumber=StringVar()

ContactNumberValue = Entry(page, textvariable=contactnumber, width=25,).place(x=500, y=203)



Alergies = tkinter.Label(page, text='v List any medications, allergies,\n or other physical conditions the Camp Director should be aware of:', font=('arial')).place(x=325, y=260)

alergies=StringVar()

AlergiesValue = Entry(page, textvariable=alergies,width=100).place(x=300, y=300)


#creating dd menu
grade = tkinter.StringVar()
Grade = tkinter.Label(page, text='Grade:', font=('arial')).place(x=136, y=260)
GradeValue = tkinter.OptionMenu(page, grade, 'Pre K', 'Kindergarten', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', 'Graduate')
GradeValue.configure(font='arial')
GradeValue.place(x=200, y=256)

gender = tkinter.StringVar()
Gender = tkinter.Label(page, text='Gender:', font=('arial')).place(x=136, y=313)
GenderValue = tkinter.OptionMenu(page, gender, 'Male', 'Female')
GenderValue.configure(font='arial')
GenderValue.place(x=200, y=310)

married = tkinter.StringVar()
Married = tkinter.Label(page, text='Married?:', font=('arial')).place(x=122, y=366)
GenderValue = tkinter.OptionMenu(page, married, 'Yes', 'No')
GenderValue.configure(font='arial')
GenderValue.place(x=200, y=360)

room = tkinter.StringVar()
Room = tkinter.Label(page, text='Room:', font=('arial')).place(x=700, y=50)
RoomValue = tkinter.OptionMenu(page, room, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
RoomValue.configure(font='arial')
RoomValue.place(x=775, y=45)

counsoler = tkinter.StringVar()
Counsoler = tkinter.Label(page, text='Counsoler:', font=('arial')).place(x=675, y=102)
CounsolerValue = tkinter.OptionMenu(page, counsoler, 'Bro. Dukes', 'Bro. Surles', 'Bro. Green', 'Bro. Baccus', 'Sis. Baccus', 'Sis. Jenkins', 'Sis. Griswold')
CounsolerValue.configure(font='arial')
CounsolerValue.place(x=775, y=98)

classes = tkinter.StringVar()
Classes = tkinter.Label(page, text='Class:', font=('arial')).place(x=705, y=150)
ClassesValue = tkinter.OptionMenu(page, room, 'Teen', 'Childrens Church')
ClassesValue.configure(font='arial')
ClassesValue.place(x=775, y=145)
#button
def buttonclick():
	#heres where you lnk where you want your info to go

work = Button(page, text='Submit', width=10, height=2, bg='lightgrey', command=buttonclick()).place(x=475, y=450)

#heres where you execute your close files commands

#ending code never put this above anything
page.mainloop()