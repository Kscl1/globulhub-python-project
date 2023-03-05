import csv
import datetime
import pandas as pd
from tkinter import *

from tkinter import messagebox

BACKGROUND_COLOR1="#a71c20"
BACKGROUND_COLOR2="#e3a207"
BACKGROUND_COLOR3="#16421c"
BACKGROUND_COLOR4="#0e8110"
BACKGROUND_COLOR5="#1a439a"

window = Tk()

window.title("Pizza Order")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR1)
window.geometry("800x526") 

"""
canvas = Canvas(window, width = 750, height = 600,borderwidth=10, bg = BACKGROUND_COLOR1, highlightthickness = 1)
canvas.pack()

#canvas.create_text(10, 10, text = 'Welcome', font = ('Helvetica', 72, 'bold'), justify = 'center', fill='blue')
frame = Frame(window,bg="white")
#Label(frame,text="Welcome")



 
# Add the frame to the canvas
canvas.create_window(0, 0, window=frame, anchor="nw")


"""
"""
text = Text(frame, height=8)
text.pack()

text.insert('1.0', 'This is a Text widget demo')"""
"""



canvas.create_window(10, 10, window=frame, anchor="nw")

def roundPolygon(x, y, sharpness, **kwargs):

    if sharpness < 2:
        sharpness = 2

    ratioMultiplier = sharpness - 1
    ratioDividend = sharpness

    points = []
  
    for i in range(len(x)):

        points.append(x[i])
        points.append(y[i])

        if i != (len(x) - 1):
            points.append((ratioMultiplier*x[i] + x[i + 1])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[i + 1])/ratioDividend)
            points.append((ratioMultiplier*x[i + 1] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[i + 1] + y[i])/ratioDividend)
        else:
            points.append((ratioMultiplier*x[i] + x[0])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[0])/ratioDividend)
            points.append((ratioMultiplier*x[0] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[0] + y[i])/ratioDividend)
           
            points.append(x[0])
            points.append(y[0])

    return canvas.create_polygon(points, **kwargs, smooth=TRUE)

my_rectangle = roundPolygon([10, 740, 740, 10], [10, 10, 475, 475], 20 , width=5, outline=BACKGROUND_COLOR4, fill=BACKGROUND_COLOR2)


"""



#window.messagebox()

"""user's name, user id, credit card information, description of order, time order,credit card password"""


#for pizzas
#canvas.create_window(10, 10, window=frame, anchor="nw")

"""
#left_frame2 = Frame(window)
#frame.config("padx"=(5,10,5,10))
frame.pack(side="left", fill="both", expand=True)
#frame.grid_rowconfigure((2,2,2,2))
frame.grid_columnconfigure((0,1,2,3), weight=1, uniform="equal")

"""



canvas = Canvas(window, height=800, width=800, background=BACKGROUND_COLOR2)
canvas.pack(side="left")
 
# Create a frame
frame = Frame(window, bg="#eeeeee",width=400,height=200)
frame.pack(side="top", fill="both", expand=True)

# Add the frame to the canvas
canvas.create_window(20, 60, window=frame, anchor="nw")

canvas.create_text(150,30,text="Pizza Types",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3)

canvas.create_text(150,220,text="Sauce Types",font = ('Arial', 15, 'bold'), justify = 'center', fill=BACKGROUND_COLOR3)
 
frame.grid_columnconfigure((0,1), weight=1,uniform ="equal")

var = IntVar()
Radiobutton(frame,text='Classic        ', variable=var,value=1).grid(row=1,column=0,sticky="nw")
Radiobutton(frame,text='Margherita       ', variable=var,value=2).grid(row=1,column=1,sticky="nw")
Radiobutton(frame,text='Turk   Pizza', variable=var,value=3).grid(row=2,column=0,sticky="nw")
Radiobutton(frame,text='Dominos Pizza ', variable=var,value=4).grid(row=2,column=1,sticky="nw")

#messagebox.showinfo("Information","Information for user")
#Misc.lift()"""









#w = CheckButton(master, option=value)


#for sauces (6)
#w = RadioButton(master, option=value)






def func():
    return






""" 
btn=Button(window,text="Order", width=10,height=3,command=func)
btn.place(x=95,y=50)"""


#canvas.grid(rowspan=4,columnspan=6)


window.mainloop()

