import csv
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pizza import *
from decorator import *


#MENU DATAS

menu =[]

with open ("menu.txt", "r") as file:
    data = file.readlines()
    
for i in range(len(data)):
    if 1<=i<=2:
        menu.append(data[i].split()[1])
        
    elif 3<=i<=4:
        menu.append(data[i].split()[1]+" "+data[i].split()[2])
        
    elif 6<=i<8:
        menu.append(data[i].split()[1])
    elif i == 8: 
        menu.append(data[i].split()[1]+" "+data[i].split()[2])
    elif 9<=i<=11:
        menu.append(data[i].split()[1])



#BACKGROUND

BACKGROUND_COLOR1="#a71c20"
BACKGROUND_COLOR2="#e3a207"
BACKGROUND_COLOR3="#16421c"
BACKGROUND_COLOR4="#f2f2f2"


window = Tk()
window.title("Pizza Order")
window.config(padx=30,pady=30,bg=BACKGROUND_COLOR1)
window.geometry("800x526") 

canvas = Canvas(window, height=1200, width=500, background=BACKGROUND_COLOR2)
canvas.pack(side = LEFT,fill = BOTH,expand = 1)
 

# FRAMES

pizzaframe = Frame(canvas,bg=BACKGROUND_COLOR2, width=200)
pizzaframe.pack()

sauceframe = Frame(canvas,bg=BACKGROUND_COLOR4,width=200)
sauceframe.pack(side = LEFT)

menuframe = Frame(canvas,bg = BACKGROUND_COLOR2)
menuframe.pack(side = RIGHT)

paymentframe = Frame(canvas,bg = BACKGROUND_COLOR2)
paymentframe.pack(side=BOTTOM)


#FRAME WINDOWS AND TITLES

canvas.create_window((60, 60), window = pizzaframe, anchor="nw")
canvas.create_window((60, 215), window = sauceframe, anchor="nw")
canvas.create_window((525, 60), window = menuframe, anchor="nw")
canvas.create_window((160, 490), window = paymentframe, anchor="nw")


canvas.create_text(250,40,text="Pizzas",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3)
canvas.create_text(250,195,text="Sauces",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3)
canvas.create_text(590,40,text="Menu",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3) 
canvas.create_text(360,460,text="Payment Information",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3) 

pizzaframe.grid_columnconfigure((0,1), weight=1,uniform ="equal")
sauceframe.grid_columnconfigure((0,1), weight=1,uniform ="equal")
paymentframe.grid_columnconfigure((0), weight=1,uniform ="equal")

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
    4:"Plain Pizza"
        }

order_pizza=""

def AddPizza():
    global order_pizza
    if(len(data_dict["description_of_order"])==0):
        data_dict["description_of_order"].append(rbdict[var.get()])
        order_pizza=rbdict[var.get()]
    else:
        data_dict["description_of_order"][0]=rbdict[var.get()]
        order_pizza=rbdict[var.get()]
            
var = IntVar()

Radiobutton(pizzaframe,text='Classic        ', variable=var,height = 2, width = 20, value=1, command = AddPizza).grid(row=1,column=0,sticky="nw")

Radiobutton(pizzaframe, text='Margherita       ', variable=var, height = 2, width = 20, value=2, command = AddPizza).grid(row=1,column=1,sticky="nw")

Radiobutton(pizzaframe, text='Turk   Pizza', variable=var, height = 2, width = 20, value=3, command = AddPizza).grid(row=2,column=0,sticky="nw")

Radiobutton(pizzaframe, text='Plain Pizza         ', variable=var, height = 2, width = 20, value = 4, command = AddPizza).grid(row=2,column=1,sticky="nw")

#CHECKBUTTONS

sauce_list=[]
flag = 0 

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
        sauce_list.append(data_dict["description_of_order"][0])
        for value in rbdict.values():
            for i in sauce_list:
                if i!=order_pizza and i==value:
                    sauce_list.remove(i)
        a = sauce_list[0]
        b = sauce_list[len(sauce_list)-1]
        sauce_list[0]=b
        sauce_list[len(sauce_list)-1]=a
        data_dict["description_of_order"].pop(0)
        data_dict["description_of_order"].append(sauce_list)

def ChangeFlag():
    global flag
    flag=1


Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()
Checkbutton4 = IntVar()
Checkbutton5 = IntVar()
Checkbutton6 = IntVar()
Checkbutton7 = IntVar()
  
Button1 = Checkbutton(sauceframe, text = "Olives         ", variable = Checkbutton1, onvalue = 1, offvalue = 0, height = 2, width = 20, command = CheckSauce).grid(row=0,column=0,sticky="nw")
  
Button2 = Checkbutton(sauceframe, text = "Mushrooms", variable = Checkbutton2, onvalue = 1, offvalue = 0, height = 2, width = 20, command = CheckSauce).grid(row=1,column=0,sticky="nw")
  
Button3 = Checkbutton(sauceframe, text = "Goat Cheese", variable = Checkbutton3, onvalue = 1, offvalue = 0, height = 2, width = 20, command = CheckSauce).grid(row=2,column=0,sticky="nw")

Button4 = Checkbutton(sauceframe, text = "Meat    ", variable = Checkbutton4, onvalue = 1, offvalue = 0,height = 2, width = 20, command = CheckSauce).grid(row=0,column=1,sticky="nw")
Button5 = Checkbutton(sauceframe, text = "Onions ", variable = Checkbutton5, onvalue = 1, offvalue = 0, height = 2, width = 20, command = CheckSauce).grid(row=1,column=1,sticky="nw")

Button6 = Checkbutton(sauceframe, text = "Corn     ", variable = Checkbutton6, onvalue = 1, offvalue = 0, height = 2, width = 20, command = CheckSauce).grid(row=2,column=1,sticky="nw")

Button7 = Checkbutton(sauceframe, text = "I don't want sauce", variable = Checkbutton7, onvalue = 1, offvalue = 0, height = 2,width=44, command = ChangeFlag).grid(row=3,column=0,sticky="nw",columnspan=3)


#MENU

def onClick(n):
    pizzas=[Classic(),Margherita(),Turk_Pizza(),Plain_Pizza()]
    decorators=[Olives(),Mushrooms(),Goat_Cheese(),Meat(),Onions(),Corn()]
    if n<4 and menu[n] == pizzas[n].name:
        messagebox.showinfo(pizzas[n].name,pizzas[n].get_description()+ pizzas[n].get_cost())
    elif menu[n].upper() == decorators[n-4].description.upper():
        messagebox.showinfo(decorators[n-4].get_description(),decorators[n-4].get_cost())

b0=Button(menuframe,text=menu[0],width=15,height=1,command=lambda:onClick(0)).grid(row=0,column=0)
b1=Button(menuframe,text=menu[1],width=15,height=1,command=lambda:onClick(1)).grid(row=1,column=0)
b2=Button(menuframe,text=menu[2],width=15,height=1,command=lambda:onClick(2)).grid(row=2,column=0)
b3=Button(menuframe,text=menu[3],width=15,height=1,command=lambda:onClick(3)).grid(row=3,column=0)
b4=Button(menuframe,text=menu[4],width=15,height=1,command=lambda:onClick(4)).grid(row=4,column=0)
b5=Button(menuframe,text=menu[5],width=15,height=1,command=lambda:onClick(5)).grid(row=5,column=0)
b6=Button(menuframe,text=menu[6],width=15,height=1,command=lambda:onClick(6)).grid(row=6,column=0)
b7=Button(menuframe,text=menu[7],width=15,height=1,command=lambda:onClick(7)).grid(row=7,column=0)
b8=Button(menuframe,text=menu[8],width=15,height=1,command=lambda:onClick(8)).grid(row=8,column=0)
b9=Button(menuframe,text=menu[9],width=15,height=1,command=lambda:onClick(9)).grid(row=9,column=0)


#INFORMATIONS

def SaveName(name):
    data_dict["users_name"]=name.get()
    
def SaveId(user_id):
    data_dict["user_id"]=user_id.get()

def SaveCreditNo(creditno):
    data_dict["credit_card_information"]=creditno.get()

def SavePassword(password):
    data_dict["credit_card_password"]=password.get()

def SaveTime():
    data_dict["time_order"]=datetime.now().strftime("%H:%M:%S")

def Calculate_Cost():
    cost = 0
    pizzas=[Classic(),Margherita(),Turk_Pizza(),Plain_Pizza()]
    global flag

    if flag == 0:
        wanted_pizza = data_dict["description_of_order"][0][0]
        decorators=[Olives(),Mushrooms(),Corn(),Goat_Cheese(),Meat(),Onions()]

        for sauce in data_dict["description_of_order"][0]:
            for d in decorators:
                if sauce == d.description:
                    cost += d.price

        for p in pizzas:
            if wanted_pizza == p.name:
                cost += p.price
    else:
        wanted_pizza = data_dict["description_of_order"][0]
        print(wanted_pizza)
        for p in pizzas:
            if wanted_pizza == p.name:
                cost += p.price

    return cost


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

def reset_buttons():
    var.set(None)
    Checkbutton1.set(0)
    Checkbutton2.set(0)
    Checkbutton3.set(0)
    Checkbutton4.set(0)
    Checkbutton5.set(0)
    Checkbutton6.set(0)
    Checkbutton7.set(0)
    name.set("")
    user_id.set("")
    creditno.set("") 
    password.set("")

    global data_dict
    global order_pizza
    global sauce_list
    global flag

    data_dict= {"users_name":"", "user_id":0, "credit_card_information":0, "description_of_order":[], "time_order":"", "credit_card_password":0}
    
    order_pizza = ""
    sauce_list = []
    flag = 0


CheckSauce()
def Order():
    SaveSauce()
    SaveName(name)
    SaveId(user_id)
    SaveCreditNo(creditno)
    SavePassword(password)
    SaveTime()
    

    with open('Orders_Database.csv','a',newline='') as file:
        fields = ["users_name", "user_id", "credit_card_information", "description_of_order", "time_order","credit_card_password"]
        writer = csv.DictWriter(file,fieldnames = fields)
        writer.writerow(data_dict)
    messagebox.showinfo("Complete your payment ","Your order costs "+str(Calculate_Cost())+" Turkish Liras.\nEnjoy your meal!")
    reset_buttons()
        

order_button = Button(paymentframe,
                      text = "Order",
                      width = 20,
                      height = 2,
                      command = Order) 
order_button.grid(row=9,column=0,columnspan=2)


window.mainloop()

