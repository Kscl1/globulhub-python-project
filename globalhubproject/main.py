import csv
from datetime import datetime
import pandas as pd
from tkinter import *
from tkinter import ttk
from pizza import *
from decorator import *


"""user's name, user id, credit card information, description of order, time order,credit card password"""


#MENU DATAS

menu =[]

with open ("menu.txt", "r") as file:
    data = file.readlines()

for i in range(len(data)):
    if 1<=i<=4:
        menu.append(data[i].split()[1])

    elif 6<=i<=11:
        menu.append(data[i].split()[1])

#BACKGROUND

BACKGROUND_COLOR1="#a71c20"
BACKGROUND_COLOR2="#e3a207"
BACKGROUND_COLOR3="#16421c"
BACKGROUND_COLOR4="#0e8110"
BACKGROUND_COLOR5="#1a439a"
BACKGROUND_COLOR6="#f2f2f2"


window = Tk()
window.title("Pizza Order")
window.config(padx=30,pady=30,bg=BACKGROUND_COLOR1)
window.geometry("800x526") 

canvas = Canvas(window, height=1200, width=500, background=BACKGROUND_COLOR2)
canvas.pack(side = LEFT,fill = BOTH,expand = 1)
 

# FRAMES

pizzaframe = Frame(canvas,bg=BACKGROUND_COLOR2, width=200)
pizzaframe.pack()

sauceframe = Frame(canvas,bg=BACKGROUND_COLOR2,width=200)
sauceframe.pack(side = LEFT)

menuframe = Frame(canvas,bg = BACKGROUND_COLOR2)
menuframe.pack(side = RIGHT)

paymentframe = Frame(canvas,bg = BACKGROUND_COLOR2)
paymentframe.pack(side=BOTTOM)


#FRAME WINDOWS AND TITLES

canvas.create_window((60, 60), window = pizzaframe, anchor="nw")
canvas.create_window((60, 225), window = sauceframe, anchor="nw")
canvas.create_window((550, 60), window = menuframe, anchor="nw")
canvas.create_window((160, 500), window = paymentframe, anchor="nw")


canvas.create_text(230,35,text="Pizzas",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3)
canvas.create_text(230,195,text="Sauces",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3)
canvas.create_text(595,35,text="Menu",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3) 
canvas.create_text(360,450,text="Payment Information",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3) 

pizzaframe.grid_columnconfigure((0,1), weight=1,uniform ="equal")
sauceframe.grid_columnconfigure((0,1), weight=1,uniform ="equal")


l=Label(paymentframe,text="",bg=BACKGROUND_COLOR2)
l.grid(row=8,column=0)

l2=Label(paymentframe,text="",bg=BACKGROUND_COLOR2)
l2.grid(row=10,column=0)


#SCROLLBAR

sbar = ttk.Scrollbar(window, orient=VERTICAL, command=canvas.yview)
sbar.pack(side=RIGHT,fill=Y)

canvas.configure(yscrollcommand=sbar.set)
canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

def _on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
canvas.bind_all("<MouseWheel>", _on_mouse_wheel)


#RADIOBUTTONS

data_dict= {
    "users_name":"",
    "user_id":0,
    "credit_card_information":0,
    "description_of_order":[],
    "time_order":"",
    "credit_card_password":0
            }
rbdict= {
    1:"Classic",
    2:"Margherita",
    3:"Turk Pizza",
    4:"Dominos Pizza"
        }

def AddPizza():
    if(len(data_dict["description_of_order"])==0):
        data_dict["description_of_order"].append(rbdict[var.get()])
    else:
        data_dict["description_of_order"]=rbdict[var.get()]
            
var = IntVar()

Radiobutton(pizzaframe,text='Classic        ', variable=var,height = 2, width = 18, value=1, command = AddPizza).grid(row=1,column=0,sticky="nw")

Radiobutton(pizzaframe, text='Margherita       ', variable=var, height = 2, width = 18, value=2, command = AddPizza).grid(row=1,column=1,sticky="nw")

Radiobutton(pizzaframe, text='Turk   Pizza', variable=var, height = 2, width = 18, value=3, command = AddPizza).grid(row=2,column=0,sticky="nw")

Radiobutton(pizzaframe, text='Dominos Pizza ', variable=var, height = 2, width = 18, value = 4, command = AddPizza).grid(row=2,column=1,sticky="nw")

#CHECKBUTTONS

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
    elif Checkbutton6.get() == 1 and "Corn" not in sauce_list:
        sauce_list.append("Corn")

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
    elif Checkbutton6.get() == 0 and "Corn" in sauce_list:
        sauce_list.remove("Corn")

def CheckSauce():
    AddSauce()
    DeleteSauce()
    
    
def SaveSauce():
    if len(sauce_list)!=0:
        print(data_dict["description_of_order"])
        sauce_list.append(data_dict["description_of_order"][0])
        print(sauce_list)
        a = sauce_list[0]
        b = sauce_list[len(sauce_list)-1]
        sauce_list[0]=b
        sauce_list[len(sauce_list)-1]=a
        data_dict["description_of_order"].pop(0)
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
  
Button1 = Checkbutton(sauceframe, text = "Olives         ", variable = Checkbutton1, onvalue = 1, offvalue = 0, height = 2, width = 18, command = CheckSauce).grid(row=0,column=0,sticky="nw")
  
Button2 = Checkbutton(sauceframe, text = "Mushrooms", variable = Checkbutton2, onvalue = 1, offvalue = 0, height = 2, width = 18, command = CheckSauce).grid(row=1,column=0,sticky="nw")
  
Button3 = Checkbutton(sauceframe, text = "Goat Cheese", variable = Checkbutton3, onvalue = 1, offvalue = 0, height = 2, width = 18, command = CheckSauce).grid(row=2,column=0,sticky="nw")

Button4 = Checkbutton(sauceframe, text = "Meat    ", variable = Checkbutton4, onvalue = 1, offvalue = 0,height = 2, width = 18, command = CheckSauce).grid(row=0,column=1,sticky="nw")
Button5 = Checkbutton(sauceframe, text = "Onions ", variable = Checkbutton5, onvalue = 1, offvalue = 0, height = 2, width = 18, command = CheckSauce).grid(row=1,column=1,sticky="nw")

Button6 = Checkbutton(sauceframe, text = "Corn     ", variable = Checkbutton6, onvalue = 1, offvalue = 0, height = 2, width = 18, command = CheckSauce).grid(row=2,column=1,sticky="nw")


#MENU

counter=0
for counter in range(len(menu)):
    l1=Button(menuframe,text=menu[counter],width=10,height=1)
    l1.grid(row=counter,column=0)




"""
def click():
    check.config(state=DISABLED)
check = Checkbutton(text="Click Me", command=click)"""


"""btn=Button(window,text="Order", width=10,height=3,command=func)"""

#INFORMATIONS

"""user's name, user id, credit card information, description of order, time order,credit card password"""

def SaveName(name):
    data_dict["users_name"]=name.get()
    datdict_df = pd.DataFrame(data_dict)
    datdict_df.to_csv("Orders_Database.csv",index=False)
    

def SaveId(user_id):
    data_dict["user_id"]=user_id.get()
    datdict_df = pd.DataFrame(data_dict)
    datdict_df.to_csv("Orders_Database.csv",index=False)

def SaveCreditNo(creditno):
    data_dict["credit_card_information"]=creditno.get()
    datdict_df = pd.DataFrame(data_dict)
    datdict_df.to_csv("Orders_Database.csv",index=False)

def SavePassword(password):
    data_dict["credit_card_password"]=password.get()
    datdict_df = pd.DataFrame(data_dict)
    datdict_df.to_csv("Orders_Database.csv",index=False)

def SaveTime():
    data_dict["time_order"]=datetime.now().strftime("%H:%M:%S")
    datdict_df = pd.DataFrame(data_dict)
    datdict_df.to_csv("Orders_Database.csv",index=False)

def Calculate_Cost():
    
    cost = 0
    wanted_pizza = data_dict["description_of_order"][0][0]
    pizzas=[Classic(),Margherita(),Turk_Pizza(),Dominos_Pizza()]
    decorators=[Olives(),Mushrooms(),Corn(),Goat_Cheese(),Meat(),Onions()]

    for sauce in data_dict["description_of_order"][0]:
        for d in decorators:
            if sauce == d.description:
                cost += d.price

    for p in pizzas:
        if wanted_pizza == p.name:
            cost += p.price
            
        
    print(cost)




name = StringVar()
user_id = StringVar()
creditno = StringVar()
password = StringVar()

name_label = Label(paymentframe, text = "Name",height=1,width=50).grid(row=0,column=0)
user_id_label = Label(paymentframe, text = "Id",height=1,width=50).grid(row=2,column=0)
name_en = Entry(paymentframe,width=50, textvariable=name).grid(row=1,column=0)
id_en = Entry(paymentframe,width=50, textvariable=user_id).grid(row=3,column=0)

creditno_label = Label(paymentframe, text = "Credit Cart Info",height=1,width=50).grid(row=4,column=0)
password_label= Label(paymentframe, text = "Password",height=1,width=50).grid(row=6,column=0)
creditno_en = Entry(paymentframe,width=50,textvariable=creditno).grid(row=5,column=0)
password_en = Entry(paymentframe,width=50,textvariable=password).grid(row=7,column=0)


#ORDER

CheckSauce()
def Order():
    SaveSauce()
    SaveName(name)
    SaveId(user_id)
    SaveCreditNo(creditno)
    SavePassword(password)
    SaveTime()
    Calculate_Cost()

def reset_buttons():

    var.set(None)
    Checkbutton1.set(None)
    Checkbutton2.set(None)
    Checkbutton3.set(None)
    Checkbutton4.set(None)
    Checkbutton5.set(None)
    Checkbutton6.set(None)
    name.set("")
    user_id.set("")
    creditno.set("") 
    password.set("")
    global data_dict

    data_dict= {
    "users_name":"",
    "user_id":0,
    "credit_card_information":0,
    "description_of_order":[],
    "time_order":"",
    "credit_card_password":0
            }

order_button = Button(paymentframe,
                      text = "Order",
                      width = 20,
                      height = 2,
                      command = lambda:[Order(),reset_buttons()])  #command = lambda:[Order(),reset_buttons()]
order_button.grid(row=9,column=0,columnspan=2)


window.mainloop()

