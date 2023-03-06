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



#RADIOBUTTONS

data_dict={"users_name":"","user_id":0,"credit_card_information":0, "description_of_order":[], "time_order":"","credit_card_password":0}
def AddPizza():
    if(len(data_dict["description_of_order"])==0):
        data_dict["description_of_order"].append(rbdict[var.get()])
        """print(data_dict["description_of_order"][0])
        datdict_df = pd.DataFrame(data_dict)
        datdict_df.to_csv("Orders_Database.csv",index=False)"""
    else:
        data_dict["description_of_order"]=rbdict[var.get()]
        """print(data_dict["description_of_order"][0])
        datdict_df = pd.DataFrame(data_dict)
        datdict_df.to_csv("Orders_Database.csv",index=False)"""
            


rbdict= {1:"Classic",2:"Margherita",3:"Turk Pizza",4:"Dominos Pizza"}

var = IntVar()

Radiobutton(frame1,
            text='Classic        ', 
            variable=var,
            height = 2,
            width = 18,
            value=1,
            command = AddPizza).grid(row=1,column=0,sticky="nw")

Radiobutton(frame1,
            text='Margherita       ', 
            variable=var,
            height = 2,
            width = 18,
            value=2,
            command = AddPizza).grid(row=1,column=1,sticky="nw")

Radiobutton(frame1,
            text='Turk   Pizza',
            variable=var,
            height = 2,
            width = 18,
            value=3,
            command = AddPizza).grid(row=2,column=0,sticky="nw")
Radiobutton(frame1,
            text='Dominos Pizza ',
            variable=var,
            height = 2,
            width = 18,
            value = 4,
            command = AddPizza).grid(row=2,column=1,sticky="nw")

#CHECKBUTTONS

"""
cbdict= {"CheckButton1":"Olives","CheckButton2":"Mushrooms","CheckButton3":"Goat Cheese","CheckButton4":"Meat","CheckButton5":"Onions","CheckButton6":"Corns"}"""

sauce_list=[]

def AddSauce():

    if Checkbutton1.get() == 1 and "Olives" not in sauce_list:
        sauce_list.append("Olives")
    elif Checkbutton2.get() == 1 and "Mushrooms" not in sauce_list:
        sauce_list.append("Mushrooms")
    elif Checkbutton3.get() == 1 and "Goat Cheese" not in sauce_list:
        sauce_list.append("Goat Cheese")
    elif Checkbutton4.get() == 1 and "Meat" not in sauce_list:
        sauce_list.append("Meat")
    elif Checkbutton5.get() == 1 and "Onions" not in sauce_list:
        sauce_list.append("Onions")
    elif Checkbutton6.get() == 1 and "Corns" not in sauce_list:
        sauce_list.append("Corns")

def DeleteSauce():

    if Checkbutton1.get() == 0 and "Olives" in sauce_list:
        sauce_list.remove("Olives")
    elif Checkbutton2.get() == 0 and "Mushrooms" in sauce_list:
        sauce_list.remove("Mushrooms")
    elif Checkbutton3.get() == 0 and "Goat Cheese" in sauce_list:
        sauce_list.remove("Goat Cheese")
    elif Checkbutton4.get() == 0 and "Meat" in sauce_list:
        sauce_list.remove("Meat")
    elif Checkbutton5.get() == 0 and "Onions" in sauce_list:
        sauce_list.remove("Onions")
    elif Checkbutton6.get() == 0 and "Corns" in sauce_list:
        sauce_list.remove("Corns")

def CheckSauce():
    AddSauce()
    DeleteSauce()
    
    

def SaveSauce():
    if len(sauce_list)!=0:
        print(data_dict["description_of_order"])
        data_dict["description_of_order"].append(sauce_list)
        print(data_dict["description_of_order"])
        datdict_df = pd.DataFrame(data_dict)
        datdict_df.to_csv("Orders_Database.csv",index=False)



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
                      width = 18,
                      command = CheckSauce).grid(row=0,column=0,sticky="nw")
  
Button2 = Checkbutton(frame2, 
                      text = "Mushrooms",
                      variable = Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18,
                      command = CheckSauce).grid(row=1,column=0,sticky="nw")
  
Button3 = Checkbutton(frame2, 
                      text = "Goat Cheese",
                      variable = Checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18,
                      command = CheckSauce).grid(row=2,column=0,sticky="nw")

Button4 = Checkbutton(frame2, 
                      text = "Meat    ",
                      variable = Checkbutton4,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18,
                      command = CheckSauce).grid(row=0,column=1,sticky="nw")
Button5 = Checkbutton(frame2, 
                      text = "Onions ",
                      variable = Checkbutton5,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18,
                      command = CheckSauce).grid(row=1,column=1,sticky="nw")
Button6 = Checkbutton(frame2, 
                      text = "Corn     ",
                      variable = Checkbutton6,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 18,
                      command = CheckSauce).grid(row=2,column=1,sticky="nw")


#MENU

counter=0
for counter in range(len(menu)):
    l1=Button(frame3,text=menu[counter],width=10,height=1)
    l1.grid(row=counter,column=0)



#ORDER
CheckSauce()
def Order():
    SaveSauce()
def reset_buttons():
    if Button1.state!="normal":
        Button1.state="normal"



order_button = Button(frame2,
                      text = "Order",
                      width = 10,
                      height = 2,
                      command = Order)          #command = lambda:[Order(),reset_buttons()])
order_button.grid(row=4,column=0,columnspan=2)

"""
def click():
    check.config(state=DISABLED)
check = Checkbutton(text="Click Me", command=click)"""




window.mainloop()



