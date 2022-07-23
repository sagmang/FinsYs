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
root.title('Finsys-Invoices')
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
label_1 = Label(canvas,width=10,height=1,text="INVOICES", font=('arial 25'),background="#1b3857",fg="white") 
window_label_1 = canvas.create_window(550, 85, anchor="nw", window=label_1)
canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

my_rectangle_1 = round_rectangle(20, 250, 1300, 600, radius=20, fill="#1b3857")


# s = ttk.Style()
# s.configure('mystyle_2.Treeview.Heading', background='lime', State='DISABLE')
# tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5", "c6", "c7", "c8"), show='headings',height= 0, style='mystyle_2.Treeview')   
# tree.column("# 1", anchor=E, stretch=NO, width=150)
# tree.heading("# 1", text="INVOICE NO")
# tree.column("# 2", anchor=E, stretch=NO, width=150)
# tree.heading("# 2", text="INVOICE DATE")
# tree.column("# 3", anchor=E, stretch=NO, width=150)
# tree.heading("# 3", text="CUSTOMER")
# tree.column("# 4", anchor=E, stretch=NO, width=150)
# tree.heading("# 4", text="EMAIL ID")
# tree.column("# 5", anchor=E, stretch=NO, width=150)
# tree.heading("# 5", text="DUE DATE")    
# tree.column("# 6", anchor=E, stretch=NO, width=150)
# tree.heading("# 6", text="GRAND TOTAL")    
# tree.column("# 7", anchor=E, stretch=NO, width=150)
# tree.heading("# 7", text="BALANCE DUE")    
# tree.column("# 8", anchor=E, stretch=NO, width=150)
# tree.heading("# 8", text="ACTION")    
# window = canvas.create_window(60, 350, anchor="nw", window=tree)
canvas.create_line(60, 350, 1260, 350, fill='gray',width=1)
canvas.create_line(60, 350, 60, 400, fill='gray',width=1)
canvas.create_line(210, 350, 210, 400, fill='gray',width=1)
canvas.create_line(360, 350, 360, 400, fill='gray',width=1)
canvas.create_line(510, 350, 510, 400, fill='gray',width=1)
canvas.create_line(660, 350, 660, 400, fill='gray',width=1)
canvas.create_line(810, 350, 810, 400, fill='gray',width=1)
canvas.create_line(960, 350, 960, 400, fill='gray',width=1)
canvas.create_line(1110, 350, 1110, 400, fill='gray',width=1)
canvas.create_line(1260, 350, 1260, 400, fill='gray',width=1)

label_2 = Label(canvas,width=10,height=1,text="INVOICE NO", font=('arial 10'),background="#1b3857",fg="white") 
window_label_2 = canvas.create_window(90, 365, anchor="nw", window=label_2)
label_3 = Label(canvas,width=11,height=1,text="INVOICE DATE", font=('arial 10'),background="#1b3857",fg="white") 
window_label_3 = canvas.create_window(240, 365, anchor="nw", window=label_3)
label_4 = Label(canvas,width=11,height=1,text="CUSTOMER", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(390, 365, anchor="nw", window=label_4)
label_4 = Label(canvas,width=11,height=1,text="EMAIL ID", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(540, 365, anchor="nw", window=label_4)
label_4 = Label(canvas,width=11,height=1,text="DUE DATE", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(690, 365, anchor="nw", window=label_4)
label_4 = Label(canvas,width=11,height=1,text="GRAND TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(840, 365, anchor="nw", window=label_4)
label_4 = Label(canvas,width=11,height=1,text="BALANCE DUE", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(990, 365, anchor="nw", window=label_4)
label_4 = Label(canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(1140, 365, anchor="nw", window=label_4)


canvas.create_line(60, 400, 1260, 400, fill='gray',width=1)
canvas.create_line(60, 400, 60, 450, fill='gray',width=1)
canvas.create_line(210, 400, 210, 450, fill='gray',width=1)
canvas.create_line(360, 400, 360, 450, fill='gray',width=1)
canvas.create_line(510, 400, 510, 450, fill='gray',width=1)
canvas.create_line(660, 400, 660, 450, fill='gray',width=1)
canvas.create_line(810, 400, 810, 450, fill='gray',width=1)
canvas.create_line(960, 400, 960, 450, fill='gray',width=1)
canvas.create_line(1110, 400, 1110, 450, fill='gray',width=1)
canvas.create_line(1260, 400, 1260, 450, fill='gray',width=1)


# Define the style for combobox widget
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

inv_comb_1 = ttk.Combobox(font=('arial 10'),foreground="white")
inv_comb_1['values'] = ("Actions","Edit","Delete")
inv_comb_1.current(0)
window_inv_comb_1 = canvas.create_window(1135, 410, anchor="nw", width=110,height=30,window=inv_comb_1)


canvas.create_line(60, 450, 1260, 450, fill='gray',width=1)



def add_invoice():
    inv_create = Toplevel()
    inv_create.geometry("1360x730")
    frame = Frame(inv_create, width=953, height=1000)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=0)
    canvas=Canvas(frame, bg='#2f516f', width=953, height=1000, scrollregion=(0,0,700,1800))
    
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
    label_1 = Label(canvas,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(550, 85, anchor="nw", window=label_1)
    canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

    my_rectangle = round_rectangle(20, 250, 1300, 1735, radius=20, fill="#1b3857")
    label_1 = Label(canvas,width=10,height=1,text="Fin sYs", font=('arial 20'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(550, 275, anchor="nw", window=label_1)

    label_2 = Label(canvas,width=15,height=1,text="Company name", font=('arial 16'),background="#1b3857",fg="skyblue") 
    window_label_2 = canvas.create_window(60, 330, anchor="nw", window=label_2)
    label_2 = Label(canvas,width=15,height=1,text="Company email-id", font=('arial 16'),background="#1b3857",fg="skyblue") 
    window_label_2 = canvas.create_window(68, 375, anchor="nw", window=label_2)

    label_2 = Label(canvas,width=15,height=1,text="Select Customer", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(66, 450, anchor="nw", window=label_2)

    comb_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_1['values'] = ("Select Customer",)
    comb_1.current(0)
    window_comb_1 = canvas.create_window(78, 475, anchor="nw", width=200, height=30,window=comb_1)

    def add_inv_customer():
        inv_create = Toplevel()
        inv_create.geometry("1360x730")
        frame = Frame(inv_create, width=953, height=900)
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

        comb_cus_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
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
        chkbtn1 = Checkbutton(canvas, text = "Same As Billing Address", variable = chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white")
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
        chkbtn2 = Checkbutton(canvas, text = "Agree to terms and conditions", variable = chk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white")
        chkbtn2.select()
        window_chkbtn_2 = canvas.create_window(69, 1150, anchor="nw", window=chkbtn2)

        cus_btn2=Button(canvas,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12')
        window_cus_btn2 = canvas.create_window(550, 1200, anchor="nw", window=cus_btn2)



    btn2=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_inv_customer)
    window_btn2 = canvas.create_window(285, 475, anchor="nw", window=btn2)

    label_2 = Label(canvas,width=15,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(400, 450, anchor="nw", window=label_2)

    entry_1=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_1 = canvas.create_window(450, 475, anchor="nw", height=30,window=entry_1)

    label_2 = Label(canvas,width=15,height=1,text="Invoice Date:", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(57, 550, anchor="nw", window=label_2)

    entry_1=DateEntry(canvas,width=40,justify=LEFT,foreground='white')
    window_entry_1 = canvas.create_window(80, 575, anchor="nw", height=30, window=entry_1)

    label_2 = Label(canvas,width=15,height=1,text="Terms", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(402, 550, anchor="nw", window=label_2)

    entry_1=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_1 = canvas.create_window(450, 575, anchor="nw", height=30, window=entry_1)

    label_2 = Label(canvas,width=15,height=1,text="Due Date:", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(770, 550, anchor="nw", window=label_2)

    entry_1=DateEntry(canvas,width=40,justify=LEFT,foreground='white')
    window_entry_1 = canvas.create_window(805, 575, anchor="nw", height=30, window=entry_1)

    label_2 = Label(canvas,width=15,height=1,text="Bill To:", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(35, 650, anchor="nw", window=label_2)

    # text_1=Text(canvas,width=31)
    # window_text_1 = canvas.create_window(81, 675, anchor="nw", height=150, window=text_1)
    entry_1=Entry(canvas,width=42,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_1 = canvas.create_window(81, 675, anchor="nw", height=150, window=entry_1)

    label_2 = Label(canvas,width=15,height=1,text="Place of supply", font=('arial 12'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(64, 860, anchor="nw", window=label_2)

    comb_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_2['values'] = ("Kerala","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Other Territory",)
    comb_2.current(0)
    window_comb_2 = canvas.create_window(82, 885, anchor="nw", width=251, height=30,window=comb_2)

    canvas.create_line(80, 950, 1240, 950, fill='gray',width=1)
    canvas.create_line(80, 1000, 1240, 1000, fill='gray',width=1)
    canvas.create_line(80, 1075, 1240, 1075, fill='gray',width=1)
    canvas.create_line(80, 950, 80, 1075, fill='gray',width=1)
    canvas.create_line(125, 950, 125, 1075, fill='gray',width=1)
    canvas.create_line(325, 950, 325, 1075, fill='gray',width=1)
    canvas.create_line(525, 950, 525, 1075, fill='gray',width=1)
    canvas.create_line(735, 950, 735, 1075, fill='gray',width=1)
    canvas.create_line(850, 950, 850, 1075, fill='gray',width=1)
    canvas.create_line(980, 950, 980, 1075, fill='gray',width=1)
    canvas.create_line(1100, 950, 1100, 1075, fill='gray',width=1)
    canvas.create_line(1240, 950, 1240, 1075, fill='gray',width=1)

    label_2 = Label(canvas,width=2,height=1,text="#", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(90, 970, anchor="nw", window=label_2)
    label_3 = Label(canvas,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = canvas.create_window(155, 970, anchor="nw", window=label_3)
    label_4 = Label(canvas,width=10,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(380, 970, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(580, 970, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=5,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(770, 970, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(880, 970, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=8,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(1005, 970, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=8,height=1,text="TAX (%)", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(1130, 970, anchor="nw", window=label_4)

    label_2 = Label(canvas,width=2,height=1,text="1", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(90, 1020, anchor="nw", window=label_2)

    comb_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_3['values'] = ("Select Product",)
    comb_3.current(0)
    window_comb_3 = canvas.create_window(135, 1015, anchor="nw", width=180, height=30,window=comb_3)

    entry_1=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_1 = canvas.create_window(335, 1015, anchor="nw", height=30, window=entry_1)

    entry_1=Entry(canvas,width=31,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_1 = canvas.create_window(535, 1015, anchor="nw", height=30, window=entry_1)

    entry_1=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_1 = canvas.create_window(745, 1015, anchor="nw", height=30, window=entry_1)

    entry_1=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_1 = canvas.create_window(860, 1015, anchor="nw", height=30, window=entry_1)

    entry_1=Entry(canvas,width=16,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_1 = canvas.create_window(990, 1015, anchor="nw", height=30, window=entry_1)

    comb_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_4['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
    comb_4.current(0)
    window_comb_4 = canvas.create_window(1110, 1015, anchor="nw", width=120, height=30,window=comb_4)

    canvas.create_line(80, 1150, 1240, 1150, fill='gray',width=1)
    canvas.create_line(80, 1225, 1240, 1225, fill='gray',width=1)
    canvas.create_line(80, 1300, 1240, 1300, fill='gray',width=1)
    canvas.create_line(80, 1075, 80, 1300, fill='gray',width=1)
    canvas.create_line(1240, 1075, 1240, 1300, fill='gray',width=1)
    canvas.create_line(125, 1075, 125, 1300, fill='gray',width=1)
    canvas.create_line(325, 1075, 325, 1300, fill='gray',width=1)
    canvas.create_line(525, 1075, 525, 1300, fill='gray',width=1)
    canvas.create_line(735, 1075, 735, 1300, fill='gray',width=1)
    canvas.create_line(850, 1075, 850, 1300, fill='gray',width=1)
    canvas.create_line(980, 1075, 980, 1300, fill='gray',width=1)
    canvas.create_line(1100, 1075, 1100, 1300, fill='gray',width=1)

    label_2 = Label(canvas,width=2,height=1,text="2", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(90, 1100, anchor="nw", window=label_2)

    comb_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_4['values'] = ("Select Product",)
    comb_4.current(0)
    window_comb_4 = canvas.create_window(135, 1095, anchor="nw", width=180, height=30,window=comb_4)

    entry_2=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_2 = canvas.create_window(335, 1095, anchor="nw", height=30, window=entry_2)

    entry_2_1=Entry(canvas,width=31,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_2_1 = canvas.create_window(535, 1095, anchor="nw", height=30, window=entry_2_1)

    entry_2_2=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_2_2 = canvas.create_window(745, 1095, anchor="nw", height=30, window=entry_2_2)

    entry_2_3=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_2_3 = canvas.create_window(860, 1095, anchor="nw", height=30, window=entry_2_3)

    entry_2_4=Entry(canvas,width=16,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_2_4 = canvas.create_window(990, 1095, anchor="nw", height=30, window=entry_2_4)

    comb_2_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_2_5['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
    comb_2_5.current(0)
    window_comb_2_5 = canvas.create_window(1110, 1095, anchor="nw", width=120, height=30,window=comb_2_5)


    label_2 = Label(canvas,width=2,height=1,text="3", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(90, 1170, anchor="nw", window=label_2)

    comb_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_5['values'] = ("Select Product",)
    comb_5.current(0)
    window_comb_5 = canvas.create_window(135, 1165, anchor="nw", width=180, height=30,window=comb_5)

    entry_3=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_3 = canvas.create_window(335, 1165, anchor="nw", height=30, window=entry_3)

    entry_3_1=Entry(canvas,width=31,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_3_1 = canvas.create_window(535, 1165, anchor="nw", height=30, window=entry_3_1)

    entry_3_2=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_3_2 = canvas.create_window(745, 1165, anchor="nw", height=30, window=entry_3_2)

    entry_3_3=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_3_3 = canvas.create_window(860, 1165, anchor="nw", height=30, window=entry_3_3)

    entry_3_4=Entry(canvas,width=16,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_3_4 = canvas.create_window(990, 1165, anchor="nw", height=30, window=entry_3_4)

    comb_3_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_3_5['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
    comb_3_5.current(0)
    window_comb_3_5 = canvas.create_window(1110, 1165, anchor="nw", width=120, height=30,window=comb_3_5)

    label_2 = Label(canvas,width=2,height=1,text="4", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(90, 1245, anchor="nw", window=label_2)

    comb_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_6['values'] = ("Select Product",)
    comb_6.current(0)
    window_comb_6 = canvas.create_window(135, 1240, anchor="nw", width=180, height=30,window=comb_6)

    entry_4=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_4 = canvas.create_window(335, 1240, anchor="nw", height=30, window=entry_4)

    entry_4_1=Entry(canvas,width=31,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_4_1 = canvas.create_window(535, 1240, anchor="nw", height=30, window=entry_4_1)

    entry_4_2=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_4_2 = canvas.create_window(745, 1240, anchor="nw", height=30, window=entry_4_2)

    entry_4_3=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_4_3 = canvas.create_window(860, 1240, anchor="nw", height=30, window=entry_4_3)

    entry_4_4=Entry(canvas,width=16,justify=LEFT,background='#2f516f',foreground="white")
    window_entry_4_4 = canvas.create_window(990, 1240, anchor="nw", height=30, window=entry_4_4)

    comb_4_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
    comb_4_5['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
    comb_4_5.current(0)
    window_comb_4_5 = canvas.create_window(1110, 1240, anchor="nw", width=120, height=30,window=comb_4_5)

    canvas.create_line(850, 1350, 1240, 1350, fill='gray',width=1)
    canvas.create_line(850, 1400, 1240, 1400, fill='gray',width=1)
    canvas.create_line(850, 1450, 1240, 1450, fill='gray',width=1)
    canvas.create_line(850, 1500, 1240, 1500, fill='gray',width=1)
    canvas.create_line(850, 1550, 1240, 1550, fill='gray',width=1)
    canvas.create_line(850, 1600, 1240, 1600, fill='gray',width=1)
    canvas.create_line(850, 1350, 850, 1600, fill='gray',width=1)
    canvas.create_line(1000, 1350, 1000, 1600, fill='gray',width=1)
    canvas.create_line(1240, 1350, 1240, 1600, fill='gray',width=1)

    label_5 = Label(canvas,width=12,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_5 = canvas.create_window(870, 1365, anchor="nw", window=label_5)
    label_5 = Label(canvas,width=12,height=1,text="Tax Amount", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_5 = canvas.create_window(870, 1415, anchor="nw", window=label_5)
    label_5 = Label(canvas,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_5 = canvas.create_window(870, 1465, anchor="nw", window=label_5)
    label_5 = Label(canvas,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_5 = canvas.create_window(870, 1515, anchor="nw", window=label_5)
    label_5 = Label(canvas,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_5 = canvas.create_window(870, 1565, anchor="nw", window=label_5)

    sub_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
    window_sub_entry_1 = canvas.create_window(1010, 1360, anchor="nw", height=30, window=sub_entry_1)

    tax_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
    window_tax_entry_1 = canvas.create_window(1010, 1410, anchor="nw", height=30, window=tax_entry_1)

    grand_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
    window_grand_entry_1 = canvas.create_window(1010, 1460, anchor="nw", height=30, window=grand_entry_1)

    amount_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
    window_amount_entry_1 = canvas.create_window(1010, 1510, anchor="nw", height=30, window=amount_entry_1)

    bal_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
    window_bal_entry_1 = canvas.create_window(1010, 1560, anchor="nw", height=30, window=bal_entry_1)


    btn1=Button(canvas,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12')
    window_btn1 = canvas.create_window(1050, 1625, anchor="nw", window=btn1)
    

btn1=Button(text='Add Invoices', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_invoice)
window_btn1 = canvas.create_window(1050, 275, anchor="nw", window=btn1)


# run the application
root.mainloop()