from datetime import date
from sqlite3 import Date
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from turtle import bgcolor, color
from tkcalendar import DateEntry

# create the root window
root = Tk()
root.title('Finsys-Customer')
root.resizable(False, False)
root.geometry("1360x730")
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)

frame = Frame(root, width=1325, height=800)
frame.pack(expand=True, fill=BOTH)
frame.place(x=2,y=0)
canvas=Canvas(frame, bg='#2f516f', width=1325, height=800, scrollregion=(0,0,700,1200))

vertibar=Scrollbar(frame, orient=VERTICAL)
vertibar.pack(side=RIGHT,fill=Y)
vertibar.config(command=canvas.yview)
canvas.config(width=1325,height=720)

canvas.config(yscrollcommand=vertibar.set)
canvas.pack(expand=True,side=LEFT,fill=BOTH)

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
 
    return canvas.create_polygon(points, **kwargs, smooth=True)
 
my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
label_1 = Label(canvas,width=12,height=1,text="CUSTOMERS", font=('arial 25'),background="#1b3857",fg="white") 
window_label_1 = canvas.create_window(550, 85, anchor="nw", window=label_1)
canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

my_rectangle_1 = round_rectangle(20, 250, 1300, 600, radius=20, fill="#1b3857")


canvas.create_line(60, 350, 1260, 350, fill='gray',width=1)
canvas.create_line(60, 350, 60, 400, fill='gray',width=1)
canvas.create_line(210, 350, 210, 400, fill='gray',width=1)
canvas.create_line(490, 350, 490, 400, fill='gray',width=1)
canvas.create_line(640, 350, 640, 400, fill='gray',width=1)
canvas.create_line(800, 350, 800, 400, fill='gray',width=1)
canvas.create_line(970, 350, 970, 400, fill='gray',width=1)
canvas.create_line(1120, 350, 1120, 400, fill='gray',width=1)
canvas.create_line(1260, 350, 1260, 400, fill='gray',width=1)

label_2 = Label(canvas,width=10,height=1,text="CUSTOMER", font=('arial 10'),background="#1b3857",fg="white") 
window_label_2 = canvas.create_window(90, 365, anchor="nw", window=label_2)
label_3 = Label(canvas,width=11,height=1,text="GST TYPE", font=('arial 10'),background="#1b3857",fg="white") 
window_label_3 = canvas.create_window(300, 365, anchor="nw", window=label_3)
label_4 = Label(canvas,width=11,height=1,text="GSTIN", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(520, 365, anchor="nw", window=label_4)
label_4 = Label(canvas,width=8,height=1,text="PAN NO", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(680, 365, anchor="nw", window=label_4)
label_4 = Label(canvas,width=8,height=1,text="EMAIL ID", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(850, 365, anchor="nw", window=label_4)
label_4 = Label(canvas,width=11,height=1,text="MOBILE NO", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(1000, 365, anchor="nw", window=label_4)
label_4 = Label(canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(1140, 365, anchor="nw", window=label_4)

canvas.create_line(60, 400, 1260, 400, fill='gray',width=1)
canvas.create_line(60, 400, 60, 450, fill='gray',width=1)
canvas.create_line(210, 400, 210, 450, fill='gray',width=1)
canvas.create_line(490, 400, 490, 450, fill='gray',width=1)
canvas.create_line(640, 400, 640, 450, fill='gray',width=1)
canvas.create_line(800, 400, 800, 450, fill='gray',width=1)
canvas.create_line(970, 400, 970, 450, fill='gray',width=1)
canvas.create_line(1120, 400, 1120, 450, fill='gray',width=1)
canvas.create_line(1260, 400, 1260, 450, fill='gray',width=1)

# Define the style for combobox widget
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

cus_comb_1 = ttk.Combobox(font=('arial 10'),foreground="white")
cus_comb_1['values'] = ("Actions","Edit","Delete")
cus_comb_1.current(0)
window_cus_comb_1 = canvas.create_window(1135, 410, anchor="nw", width=110,height=30,window=cus_comb_1)


canvas.create_line(60, 450, 1260, 450, fill='gray',width=1)

def add_customer():
    cus_create = Toplevel()
    cus_create.geometry("1360x730")
    frame = Frame(cus_create, width=953, height=900)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=0)
    canvas=Canvas(frame, bg='#2f516f', width=953, height=900, scrollregion=(0,0,700,1600))
    
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)

    canvas.config(width=1325,height=720)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
    
        return canvas.create_polygon(points, **kwargs, smooth=True)

    my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
    label_1 = Label(canvas,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(550, 85, anchor="nw", window=label_1)
    canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

    my_rectangle = round_rectangle(20, 250, 1300, 1535, radius=20, fill="#1b3857")
    label_1 = Label(canvas,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(60, 275, anchor="nw", window=label_1)
    canvas.create_line(60, 330, 1260, 330, fill='gray',width=1)

    label_2 = Label(canvas,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(62, 365, anchor="nw", window=label_2)

    comb_cus_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
    comb_cus_1.current(0)
    window_comb_cus_1 = canvas.create_window(75, 395, anchor="nw", width=245, height=30,window=comb_cus_1)

    label_2 = Label(canvas,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(400, 365, anchor="nw", window=label_2)

    entry_cus_1=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_1 = canvas.create_window(410, 395, anchor="nw", height=30,window=entry_cus_1)

    label_2 = Label(canvas,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(745, 365, anchor="nw", window=label_2)

    entry_cus_2=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_2 = canvas.create_window(755, 395, anchor="nw", height=30,window=entry_cus_2)

    label_2 = Label(canvas,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(62, 465, anchor="nw", window=label_2)

    entry_cus_3=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_3 = canvas.create_window(75, 495, anchor="nw", height=30,window=entry_cus_3)

    label_2 = Label(canvas,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(395, 465, anchor="nw", window=label_2)

    cus_4=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_cus_4 = canvas.create_window(410, 495, anchor="nw", height=30,window=cus_4)

    label_2 = Label(canvas,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(62, 565, anchor="nw", window=label_2)

    comb_cus_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white",selectcolor="#2f516f")
    comb_cus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
    comb_cus_2.current(0)
    window_comb_cus_2 = canvas.create_window(75, 595, anchor="nw", width=245, height=30,window=comb_cus_2)

    label_2 = Label(canvas,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(385, 565, anchor="nw", window=label_2)

    cus_entry_str_1 = StringVar()
    entry_cus_5=Entry(canvas,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_1)
    cus_entry_str_1.set(' 29APPCK7465F1Z1')
    window_entry_cus_5 = canvas.create_window(410, 595, anchor="nw", height=30,window=entry_cus_5)

    label_2 = Label(canvas,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(740, 565, anchor="nw", window=label_2)

    cus_entry_str_2 = StringVar()
    entry_cus_6=Entry(canvas,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_2)
    cus_entry_str_2.set(' APPCK7465F')
    window_entry_cus_6 = canvas.create_window(755, 595, anchor="nw", height=30,window=entry_cus_6)

    label_2 = Label(canvas,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(71, 665, anchor="nw", window=label_2)

    entry_cus_7=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_7 = canvas.create_window(75, 695, anchor="nw", height=30,window=entry_cus_7)

    label_2 = Label(canvas,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(395, 665, anchor="nw", window=label_2)

    entry_cus_8=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_8 = canvas.create_window(410, 695, anchor="nw", height=30,window=entry_cus_8)

    label_2 = Label(canvas,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(736, 665, anchor="nw", window=label_2)

    entry_cus_9=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_9 = canvas.create_window(752, 695, anchor="nw", height=30,window=entry_cus_9)

    label_1 = Label(canvas,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(23, 775, anchor="nw", window=label_1)

    label_2 = Label(canvas,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(71, 825, anchor="nw", window=label_2)

    entry_cus_10=Entry(canvas,width=95,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_10 = canvas.create_window(75, 855, anchor="nw", height=60,window=entry_cus_10)

    label_1 = Label(canvas,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(645, 775, anchor="nw", window=label_1)

    chk_str = StringVar()
    chkbtn1 = Checkbutton(canvas, text = "Same As Billing Address", variable = chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
    chkbtn1.select()
    window_chkbtn_1 = canvas.create_window(865, 775, anchor="nw", window=chkbtn1)

    label_2 = Label(canvas,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(681, 825, anchor="nw", window=label_2)

    entry_cus_11=Entry(canvas,width=95,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_11 = canvas.create_window(685, 855, anchor="nw", height=60,window=entry_cus_11)

    label_2 = Label(canvas,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(65, 950, anchor="nw", window=label_2)

    entry_cus_12=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_12 = canvas.create_window(75, 985, anchor="nw", height=30,window=entry_cus_12)
    
    label_2 = Label(canvas,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(395, 950, anchor="nw", window=label_2)

    entry_cus_13=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_13 = canvas.create_window(400, 985, anchor="nw", height=30,window=entry_cus_13)

    label_2 = Label(canvas,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(675, 950, anchor="nw", window=label_2)

    entry_cus_14=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_14 = canvas.create_window(685, 985, anchor="nw", height=30,window=entry_cus_14)

    label_2 = Label(canvas,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(1001, 950, anchor="nw", window=label_2)

    entry_cus_15=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_15 = canvas.create_window(1010, 985, anchor="nw", height=30,window=entry_cus_15)

    label_2 = Label(canvas,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(65, 1050, anchor="nw", window=label_2)

    entry_cus_12=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_12 = canvas.create_window(75, 1085, anchor="nw", height=30,window=entry_cus_12)
    
    label_2 = Label(canvas,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(394, 1050, anchor="nw", window=label_2)

    entry_cus_13=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_13 = canvas.create_window(400, 1085, anchor="nw", height=30,window=entry_cus_13)

    label_2 = Label(canvas,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(675, 1050, anchor="nw", window=label_2)

    entry_cus_14=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_14 = canvas.create_window(685, 1085, anchor="nw", height=30,window=entry_cus_14)

    label_2 = Label(canvas,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(1001, 1050, anchor="nw", window=label_2)

    entry_cus_15=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_cus_15 = canvas.create_window(1010, 1085, anchor="nw", height=30,window=entry_cus_15)

    chk_str_1 = StringVar()
    chkbtn2 = Checkbutton(canvas, text = "Agree to terms and conditions", variable = chk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
    chkbtn2.select()
    window_chkbtn_2 = canvas.create_window(69, 1150, anchor="nw", window=chkbtn2)

    cus_btn2=Button(canvas,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12')
    window_cus_btn2 = canvas.create_window(550, 1200, anchor="nw", window=cus_btn2)

btn1=Button(text='Add Customer', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_customer)
window_btn1 = canvas.create_window(1050, 275, anchor="nw", window=btn1)

# run the application
root.mainloop()