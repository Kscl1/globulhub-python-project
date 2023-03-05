import csv
import datetime
import pandas as pd
from tkinter import *
from tkinter import messagebox

menu =[]

with open ("menu.txt", "r") as file:
    data = file.readlines()

for i in range(len(data)):
    if 1<=i<=4:
        menu.append(data[i].split()[1])

    elif 6<=i<=11:
        menu.append(data[i].split()[1])


BACKGROUND_COLOR1="#a71c20"
BACKGROUND_COLOR2="#e3a207"
BACKGROUND_COLOR3="#16421c"
BACKGROUND_COLOR4="#0e8110"
BACKGROUND_COLOR5="#1a439a"

window = Tk()

window.title("Pizza Order")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR1)
window.geometry("800x526") 


"""user's name, user id, credit card information, description of order, time order,credit card password"""


canvas = Canvas(window, height=800, width=800, background=BACKGROUND_COLOR2)
canvas.pack()
 
# FRAMES

frame1 = Frame(window,width=400,height=200)
frame1.pack(side="top", fill="both", expand=True)

frame2 = Frame(window,bg=BACKGROUND_COLOR2,width=400,height=200)
frame2.pack(side="top", fill="both", expand=True)

frame3 = Frame(window,bg = BACKGROUND_COLOR4,width=280,height=200)
frame3.pack(side="top", fill="both", expand=True)

#FRAME WINDOWS AND TITLES

canvas.create_window(20, 60, window=frame1, anchor="nw")
canvas.create_window(20, 225, window=frame2, anchor="nw")
canvas.create_window(550, 60, window=frame3, anchor="nw")

canvas.create_text(190,30,text="Pizza Types",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3)
canvas.create_text(190,195,text="Sauce Types",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3)
canvas.create_text(590,30,text="Menu",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3) 

frame1.grid_columnconfigure((0,1), weight=1,uniform ="equal")
frame2.grid_columnconfigure((0,1), weight=1,uniform ="equal")

l=Label(frame2,text="",bg=BACKGROUND_COLOR2)
l.grid(row=3,column=0)
order_button = Button(frame2,
                      text = "Order",
                      width = 10,
                      height= 2)
order_button.grid(row=4,column=0,columnspan=2)

#RADIOBUTTONS

def SaveInfo():
    df = pd.read_csv("Orders_Database.csv")
    df = pd.DataFrame(columns = ['description of order'])
    if df.empty == 1:
        df.to_csv("Orders_Database.csv", mode="a",index=3)
    else:
        print(0)







var = IntVar()

Radiobutton(frame1,
            text='Classic        ', 
            variable=var,
            height = 2,
            width = 18,
            value=1,
            command = SaveInfo).grid(row=1,column=0,sticky="nw")

Radiobutton(frame1,
            text='Margherita       ', 
            variable=var,
            height = 2,
            width = 18,
            value=2,
            command = SaveInfo).grid(row=1,column=1,sticky="nw")

Radiobutton(frame1,
            text='Turk   Pizza',
            variable=var,
            height = 2,
            width = 18,
            value=3,
            command = SaveInfo).grid(row=2,column=0,sticky="nw")
Radiobutton(frame1,
            text='Dominos Pizza ',
            variable=var,
            height = 2,
            width = 18,
            value = 4,
            command = SaveInfo).grid(row=2,column=1,sticky="nw")

#CHECKBUTTONS

Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()
Checkbutton4 = IntVar()
Checkbutton5 = IntVar()
Checkbutton6 = IntVar()
  
Button1 = Checkbutton(frame2, 
                      text = "Olives         ", 
                      variable = Checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18).grid(row=0,column=0,sticky="nw")
  
Button2 = Checkbutton(frame2, 
                      text = "Mushrooms",
                      variable = Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18).grid(row=1,column=0,sticky="nw")
  
Button3 = Checkbutton(frame2, 
                      text = "Goat Cheese",
                      variable = Checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18).grid(row=2,column=0,sticky="nw")

Button4 = Checkbutton(frame2, 
                      text = "Meat    ",
                      variable = Checkbutton4,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18).grid(row=0,column=1,sticky="nw")
Button5 = Checkbutton(frame2, 
                      text = "Onions ",
                      variable = Checkbutton5,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18).grid(row=1,column=1,sticky="nw")
Button6 = Checkbutton(frame2, 
                      text = "Corn     ",
                      variable = Checkbutton6,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18).grid(row=2,column=1,sticky="nw")

def func():
    return

#MENU
counter=0
for counter in range(len(menu)):
    l1=Button(frame3,text=menu[counter],width=10,height=1)
    l1.grid(row=counter,column=0)












"""btn=Button(window,text="Order", width=10,height=3,command=func)"""



window.mainloop()

