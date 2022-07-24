from datetime import date
from sqlite3 import Date
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from turtle import bgcolor, color
from tkcalendar import DateEntry
from PIL import ImageTk, Image, ImageFile

# create the root window
root = Tk()
root.title('Finsys-Product')
root.resizable(False, False)
root.geometry("1360x730")
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)

lowstock = PhotoImage(file="images/lowstock.png")
outofstock = PhotoImage(file="images/outofstock.png")

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
label_1 = Label(canvas,width=23,height=1,text="PRODUCT AND SERVICES", font=('arial 25'),background="#1b3857",fg="white") 
window_label_1 = canvas.create_window(480, 85, anchor="nw", window=label_1)
canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

my_rectangle_1 = round_rectangle(20, 250, 1300, 800, radius=20, fill="#1b3857")

image_1 = Image.open("images/lowstock.png")
resize_image = image_1.resize((90,90))
image_1 = ImageTk.PhotoImage(resize_image)
btlogo = Label(canvas, width=90, height=90, background="#1b3857", image = image_1) 
window_image = canvas.create_window(250, 280, anchor="nw", window=btlogo)
btlogo.photo = image_1

label_2 = Label(canvas,width=15,height=1,text="LOW STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
window_label_2 = canvas.create_window(230, 380, anchor="nw", window=label_2)

image_2 = Image.open("images/outofstock.png")
resize_image_1 = image_2.resize((90,90))
image_2 = ImageTk.PhotoImage(resize_image_1)
btlogo_1 = Label(canvas, width=90, height=90, background="#1b3857", image = image_2) 
window_image_1 = canvas.create_window(650, 280, anchor="nw", window=btlogo_1)
btlogo_1.photo = image_2

label_2 = Label(canvas,width=15,height=1,text="OUT OF STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
window_label_2 = canvas.create_window(640, 380, anchor="nw", window=label_2)


canvas.create_line(60, 500, 1260, 500, fill='gray',width=1)
canvas.create_line(60, 500, 60, 550, fill='gray',width=1)
canvas.create_line(280, 500, 280, 550, fill='gray',width=1)
canvas.create_line(640, 500, 640, 550, fill='gray',width=1)
canvas.create_line(800, 500, 800, 550, fill='gray',width=1)
canvas.create_line(970, 500, 970, 550, fill='gray',width=1)
canvas.create_line(1120, 500, 1120, 550, fill='gray',width=1)
canvas.create_line(1260, 500, 1260, 550, fill='gray',width=1)

label_2 = Label(canvas,width=10,height=1,text="TYPE", font=('arial 10'),background="#1b3857",fg="white") 
window_label_2 = canvas.create_window(125, 515, anchor="nw", window=label_2)
label_3 = Label(canvas,width=11,height=1,text="NAME", font=('arial 10'),background="#1b3857",fg="white") 
window_label_3 = canvas.create_window(410, 515, anchor="nw", window=label_3)
label_4 = Label(canvas,width=11,height=1,text="SKU", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(680, 515, anchor="nw", window=label_4)
label_4 = Label(canvas,width=8,height=1,text="HSN/SAC", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(850, 515, anchor="nw", window=label_4)
label_4 = Label(canvas,width=11,height=1,text="QUANTITY", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(1000, 515, anchor="nw", window=label_4)
label_4 = Label(canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
window_label_4 = canvas.create_window(1140, 515, anchor="nw", window=label_4)

canvas.create_line(60, 550, 1260, 550, fill='gray',width=1)
canvas.create_line(60, 550, 60, 600, fill='gray',width=1)
canvas.create_line(280, 550, 280, 600, fill='gray',width=1)
canvas.create_line(640, 550, 640, 600, fill='gray',width=1)
canvas.create_line(800, 550, 800, 600, fill='gray',width=1)
canvas.create_line(970, 550, 970, 600, fill='gray',width=1)
canvas.create_line(1120, 550, 1120, 600, fill='gray',width=1)
canvas.create_line(1260, 500, 1260, 600, fill='gray',width=1)

# Define the style for combobox widget
style= ttk.Style(canvas)
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

cus_comb_1 = ttk.Combobox(font=('arial 10'),foreground="white")
cus_comb_1['values'] = ("Actions","Edit","Delete")
cus_comb_1.current(0)
window_cus_comb_1 = canvas.create_window(1135, 560, anchor="nw", width=110,height=30,window=cus_comb_1)


canvas.create_line(60, 600, 1260, 600, fill='gray',width=1)

def add_product():
    cus_create = Toplevel()
    cus_create.geometry("1360x730")
    frame = Frame(cus_create, width=953, height=700)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=0)
    canvas=Canvas(frame, bg='#2f516f', width=953, height=700, scrollregion=(0,0,700,1000))
    
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
    label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(480, 85, anchor="nw", window=label_1)
    canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

    my_rectangle = round_rectangle(20, 250, 1300, 900, radius=20, fill="#1b3857")

    my_rectangle = round_rectangle(200, 300, 650, 550, radius=20, fill="#2f516f")

    label_1 = Label(canvas,width=10,height=1,text="Inventory", font=('arial 20'),background="#2f516f",fg="white") 
    window_label_1 = canvas.create_window(340, 350, anchor="nw", window=label_1)

    label_1 = Label(canvas,width=45,height=2,text="Inventory is the goods available for sale and raw materials \nused to produce goods available for sale.", font=('arial 12'),background="#2f516f",fg="white") 
    window_label_1 = canvas.create_window(220, 400, anchor="nw", window=label_1)

    def inv_add_item():
        cus_create = Toplevel()
        cus_create.geometry("1360x730")
        frame = Frame(cus_create, width=953, height=700)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=2,y=0)
        canvas=Canvas(frame, bg='#2f516f', width=953, height=700, scrollregion=(0,0,700,2050))
        
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
        label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(470, 85, anchor="nw", window=label_1)
        canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

        my_rectangle = round_rectangle(20, 250, 1300, 2000, radius=20, fill="#1b3857")

        my_rectangle = round_rectangle(50, 300, 1270, 450, radius=20, fill="#2f516f")
        label_1 = Label(canvas,width=10,height=2,text="INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(475, 350, anchor="nw", window=label_1)
        btn_item_1=Button(canvas,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
        window_btn_item_1 = canvas.create_window(750, 350, anchor="nw", window=btn_item_1)

        label_1 = Label(canvas,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 500, anchor="nw", window=label_1)

        entry_inv_item_1=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_1 = canvas.create_window(55, 530, anchor="nw", height=30,window=entry_inv_item_1)

        label_1 = Label(canvas,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 600, anchor="nw", window=label_1)

        str_inv_item_1 = StringVar()
        entry_inv_item_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_inv_item_1)
        str_inv_item_1.set('  Eg: N41554')
        window_entry_entry_inv_item_2 = canvas.create_window(55, 630, anchor="nw", height=30,window=entry_inv_item_2)

        label_1 = Label(canvas,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(710, 600, anchor="nw", window=label_1)

        entry_inv_item_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_2 = canvas.create_window(710, 630, anchor="nw", height=30,window=entry_inv_item_2)

        label_1 = Label(canvas,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
        window_label_1 = canvas.create_window(710, 660, anchor="nw", window=label_1)

        label_1 = Label(canvas,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(48, 710, anchor="nw", window=label_1)

        comb_inv_item_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_inv_item_1['values'] = ("Choose...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards",)
        comb_inv_item_1.current(0)
        window_comb_inv_item_1 = canvas.create_window(55, 740, anchor="nw", width=540, height=30,window=comb_inv_item_1)

        label_1 = Label(canvas,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(705, 710, anchor="nw", window=label_1)

        entry_inv_item_3=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_3 = canvas.create_window(710, 740, anchor="nw", height=30,window=entry_inv_item_3)

        label_1 = Label(canvas,width=22,height=1,text="Initial quantity on hand", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(30, 810, anchor="nw", window=label_1)

        entry_inv_item_4=Entry(canvas,width=60,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_4 = canvas.create_window(55, 840, anchor="nw", height=30,window=entry_inv_item_4)

        label_1 = Label(canvas,width=10,height=1,text="As of date", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(450, 810, anchor="nw", window=label_1)

        entry_inv_item_5=DateEntry(canvas,width=60,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_5 = canvas.create_window(460, 840, anchor="nw", height=30,window=entry_inv_item_5)

        label_1 = Label(canvas,width=14,height=1,text="Low stock alert", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(875, 810, anchor="nw", window=label_1)

        entry_inv_item_6=Entry(canvas,width=60,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_6 = canvas.create_window(885, 840, anchor="nw", height=30,window=entry_inv_item_6)

        label_1 = Label(canvas,width=22,height=1,text="Inventory asset account", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(35, 910, anchor="nw", window=label_1)

        comb_inv_item_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_inv_item_2['values'] = ("Inventory Asset",)
        comb_inv_item_2.current(0)
        window_comb_inv_item_2 = canvas.create_window(55, 940, anchor="nw", width=480, height=30,window=comb_inv_item_2)

        asset_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
        window_asset_btn = canvas.create_window(545, 940, anchor="nw", window=asset_btn)

        label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 1010, anchor="nw", window=label_1)

        entry_inv_item_7=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_7 = canvas.create_window(55, 1040, anchor="nw", height=60,window=entry_inv_item_7)

        label_1 = Label(canvas,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(45, 1140, anchor="nw", window=label_1)
        
        entry_inv_item_8=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_8 = canvas.create_window(55, 1170, anchor="nw", height=30,window=entry_inv_item_8)

        chk_str_inv_item = StringVar()
        chkbtn_inv_item_1 = Checkbutton(canvas, text = "Inclusive of tax", variable = chk_str_inv_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn_inv_item_1.select()
        window_chkbtn_inv_item_1 = canvas.create_window(55, 1205, anchor="nw", window=chkbtn_inv_item_1)

        label_1 = Label(canvas,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(703, 1140, anchor="nw", window=label_1)

        comb_inv_item_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_inv_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
        comb_inv_item_3.current(0)
        window_comb_inv_item_3 = canvas.create_window(710, 1170, anchor="nw", width=540, height=30,window=comb_inv_item_3)

        label_1 = Label(canvas,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(41, 1270, anchor="nw", window=label_1)

        comb_inv_item_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_inv_item_4['values'] = ("Choose...","Billable Expense Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales of Product Income","Uncategorised Income",)
        comb_inv_item_4.current(0)
        window_comb_inv_item_4 = canvas.create_window(55, 1300, anchor="nw", width=480, height=30,window=comb_inv_item_4)

        account_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
        window_account_btn = canvas.create_window(545, 1300, anchor="nw", window=account_btn)

        canvas.create_line(55, 1375, 1260, 1375, fill='gray',width=1)

        label_1 = Label(canvas,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(26, 1400, anchor="nw", window=label_1)

        entry_inv_item_9=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_9 = canvas.create_window(55, 1430, anchor="nw", height=60,window=entry_inv_item_9)

        label_1 = Label(canvas,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(50, 1530, anchor="nw", window=label_1)
        
        entry_inv_item_10=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_10 = canvas.create_window(55, 1560, anchor="nw", height=30,window=entry_inv_item_10)

        chk_str_inv_item_1 = StringVar()
        chkbtn_inv_item_2 = Checkbutton(canvas, text = "Inclusive of purchase tax", variable = chk_str_inv_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn_inv_item_2.select()
        window_chkbtn_inv_item_2 = canvas.create_window(55, 1600, anchor="nw", window=chkbtn_inv_item_2)

        label_1 = Label(canvas,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(700, 1530, anchor="nw", window=label_1)

        comb_inv_item_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_inv_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
        comb_inv_item_5.current(0)
        window_comb_inv_item_5 = canvas.create_window(710, 1565, anchor="nw", width=540, height=30,window=comb_inv_item_5)

        label_1 = Label(canvas,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(47, 1660, anchor="nw", window=label_1)

        comb_inv_item_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_inv_item_6['values'] = ("Cost of sales",)
        comb_inv_item_6.current(0)
        window_comb_inv_item_6 = canvas.create_window(55, 1690, anchor="nw", width=480, height=30,window=comb_inv_item_6)

        expense_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
        window_expense_btn = canvas.create_window(545, 1690, anchor="nw", window=expense_btn)

        label_1 = Label(canvas,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(52, 1760, anchor="nw", window=label_1)

        str_inv_item_2 = StringVar()
        entry_inv_item_11=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_inv_item_2)
        str_inv_item_2.set(' 0')
        window_entry_entry_inv_item_11 = canvas.create_window(55, 1790, anchor="nw", height=30,window=entry_inv_item_11)

        label_1 = Label(canvas,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(707, 1760, anchor="nw", window=label_1)

        comb_inv_item_7 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_inv_item_7['values'] = ("Select Supplier",)
        comb_inv_item_7.current(0)
        window_comb_inv_item_7 = canvas.create_window(710, 1790, anchor="nw", width=540, height=30,window=comb_inv_item_7)

        inv_sub_btn1=Button(canvas,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
        window_inv_sub_btn1 = canvas.create_window(575, 1900, anchor="nw", window=inv_sub_btn1)



    btn_1=Button(canvas,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=inv_add_item)
    window_btn_1 = canvas.create_window(330, 470, anchor="nw", window=btn_1)

    my_rectangle = round_rectangle(700, 300, 1150, 550, radius=20, fill="#2f516f")

    label_1 = Label(canvas,width=11,height=1,text="Non-Inventory", font=('arial 20'),background="#2f516f",fg="white") 
    window_label_1 = canvas.create_window(835, 350, anchor="nw", window=label_1)

    label_1 = Label(canvas,width=46,height=2,text="A non-inventory is a type of product that is procured, sold, \nconsumed in production but we do not keep inventories for it.", font=('arial 12'),background="#2f516f",fg="white") 
    window_label_1 = canvas.create_window(720, 400, anchor="nw", window=label_1)

    def non_add_item():
        cus_create = Toplevel()
        cus_create.geometry("1360x730")
        frame = Frame(cus_create, width=953, height=700)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=2,y=0)
        canvas=Canvas(frame, bg='#2f516f', width=953, height=700, scrollregion=(0,0,700,2050))
        
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
        label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(470, 85, anchor="nw", window=label_1)
        canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

        my_rectangle = round_rectangle(20, 250, 1300, 2000, radius=20, fill="#1b3857")

        my_rectangle = round_rectangle(50, 300, 1270, 450, radius=20, fill="#2f516f")
        label_1 = Label(canvas,width=15,height=2,text="NON-INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(490, 350, anchor="nw", window=label_1)
        btn_non_item_2=Button(canvas,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
        window_btn_non_item_2 = canvas.create_window(750, 350, anchor="nw", window=btn_non_item_2)

        label_1 = Label(canvas,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 500, anchor="nw", window=label_1)

        entry_non_item_1=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_entry_inv_item_1 = canvas.create_window(55, 530, anchor="nw", height=30,window=entry_non_item_1)

        label_1 = Label(canvas,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 600, anchor="nw", window=label_1)

        str_non_item_1 = StringVar()
        entry_non_iitem_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_non_item_1)
        str_non_item_1.set('  Eg: N41554')
        window_entry_non_iitem_2 = canvas.create_window(55, 630, anchor="nw", height=30,window=entry_non_iitem_2)

        label_1 = Label(canvas,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(710, 600, anchor="nw", window=label_1)

        entry_non_item_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_non_item_2 = canvas.create_window(710, 630, anchor="nw", height=30,window=entry_non_item_2)

        label_non_1 = Label(canvas,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
        window_label_non_1 = canvas.create_window(710, 660, anchor="nw", window=label_non_1)

        label_1 = Label(canvas,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(48, 710, anchor="nw", window=label_1)

        comb_inv_item_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_inv_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards","OTH Others",)
        comb_inv_item_1.current(0)
        window_comb_inv_item_1 = canvas.create_window(55, 740, anchor="nw", width=540, height=30,window=comb_inv_item_1)

        label_1 = Label(canvas,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(705, 710, anchor="nw", window=label_1)

        entry_non_item_3=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_inv_item_3 = canvas.create_window(710, 740, anchor="nw", height=30,window=entry_non_item_3)

        canvas.create_line(55, 815, 1260, 815, fill='gray',width=1)


        label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 840, anchor="nw", window=label_1)

        chk_str_non_item = StringVar()
        chkbtn_non_item = Checkbutton(canvas, text = "I sell this product/service to my customers.", variable = chk_str_non_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        window_chkbtn_non_item = canvas.create_window(55, 870, anchor="nw", window=chkbtn_non_item)

        label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 940, anchor="nw", window=label_1)

        entry_non_item_7=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_non_item_7 = canvas.create_window(55, 970, anchor="nw", height=60,window=entry_non_item_7)

        label_1 = Label(canvas,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(45, 1070, anchor="nw", window=label_1)
        
        entry_non_item_8=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_non_item_8 = canvas.create_window(55, 1100, anchor="nw", height=30,window=entry_non_item_8)

        chk_str_non_item_1 = StringVar()
        chkbtn_non_item_1 = Checkbutton(canvas, text = "Inclusive of tax", variable = chk_str_non_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn_non_item_1.select()
        window_chkbtn_non_item_1 = canvas.create_window(55, 1135, anchor="nw", window=chkbtn_non_item_1)

        label_1 = Label(canvas,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(703, 1070, anchor="nw", window=label_1)

        comb_non_item_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_non_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
        comb_non_item_3.current(0)
        window_comb_non_item_3 = canvas.create_window(710, 1100, anchor="nw", width=540, height=30,window=comb_non_item_3)

        label_1 = Label(canvas,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(41, 1180, anchor="nw", window=label_1)

        comb_non_item_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_non_item_4['values'] = ("Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discount","Sales of Product Income","Services","Unapplied Cash Payment Income","Uncategorised Income",)
        comb_non_item_4.current(0)
        window_comb_non_item_4 = canvas.create_window(55, 1210, anchor="nw", width=480, height=30,window=comb_non_item_4)

        account_non_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
        window_account_non_btn = canvas.create_window(545, 1210, anchor="nw", window=account_non_btn)

        canvas.create_line(55, 1275, 1260, 1275, fill='gray',width=1)

        label_1 = Label(canvas,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(26, 1300, anchor="nw", window=label_1)

        chk_str_non_pitem = StringVar()
        chkbtn_non_pitem = Checkbutton(canvas, text = "I Purchase this product/service from Supplier.", variable = chk_str_non_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        window_chkbtn_non_pitem = canvas.create_window(55, 1330, anchor="nw", window=chkbtn_non_pitem)


        label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 1400, anchor="nw", window=label_1)

        entry_non_item_9=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_non_item_9 = canvas.create_window(55, 1430, anchor="nw", height=60,window=entry_non_item_9)

        label_1 = Label(canvas,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(50, 1530, anchor="nw", window=label_1)
        
        entry_non_item_10=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_non_item_10 = canvas.create_window(55, 1560, anchor="nw", height=30,window=entry_non_item_10)

        chk_str_non_item_2 = StringVar()
        chkbtn_non_item_2 = Checkbutton(canvas, text = "Inclusive of purchase tax", variable = chk_str_non_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn_non_item_2.select()
        window_chkbtn_non_item_2 = canvas.create_window(55, 1600, anchor="nw", window=chkbtn_non_item_2)

        label_1 = Label(canvas,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(700, 1530, anchor="nw", window=label_1)

        comb_non_item_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_non_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
        comb_non_item_5.current(0)
        window_comb_non_item_5 = canvas.create_window(710, 1565, anchor="nw", width=540, height=30,window=comb_non_item_5)

        label_1 = Label(canvas,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(47, 1660, anchor="nw", window=label_1)

        comb_non_item_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_non_item_6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
        comb_non_item_6.current(0)
        window_comb_non_item_6 = canvas.create_window(55, 1690, anchor="nw", width=330, height=30,window=comb_non_item_6)

        expense_non_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
        window_expense_non_btn = canvas.create_window(395, 1690, anchor="nw", window=expense_non_btn)

        label_1 = Label(canvas,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(520, 1660, anchor="nw", window=label_1)

        str_non_item_2 = StringVar()
        entry_non_item_11=Entry(canvas,width=50,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_non_item_2)
        str_non_item_2.set(' 0')
        window_entry_non_item_11 = canvas.create_window(520, 1690, anchor="nw", height=30,window=entry_non_item_11)

        label_1 = Label(canvas,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(897, 1660, anchor="nw", window=label_1)

        comb_non_item_7 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_non_item_7['values'] = ("Select Supplier",)
        comb_non_item_7.current(0)
        window_comb_non_item_7 = canvas.create_window(900, 1690, anchor="nw", width=345, height=30,window=comb_non_item_7)

        non_sub_btn1=Button(canvas,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
        window_non_sub_btn1 = canvas.create_window(575, 1800, anchor="nw", window=non_sub_btn1)

    btn_2=Button(canvas,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=non_add_item)
    window_btn_2 = canvas.create_window(830, 470, anchor="nw", window=btn_2)

    my_rectangle = round_rectangle(200, 600, 650, 850, radius=20, fill="#2f516f")

    label_1 = Label(canvas,width=10,height=1,text="Services", font=('arial 20'),background="#2f516f",fg="white") 
    window_label_1 = canvas.create_window(340, 650, anchor="nw", window=label_1)

    label_1 = Label(canvas,width=45,height=2,text="A service is a transaction in which no physical goods are \ntransferred from the seller to the buyer.", font=('arial 12'),background="#2f516f",fg="white") 
    window_label_1 = canvas.create_window(220, 700, anchor="nw", window=label_1)

    def ser_add_item():
        cus_create = Toplevel()
        cus_create.geometry("1360x730")
        frame = Frame(cus_create, width=953, height=700)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=2,y=0)
        canvas=Canvas(frame, bg='#2f516f', width=953, height=700, scrollregion=(0,0,700,2050))
        
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
        label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(470, 85, anchor="nw", window=label_1)
        canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

        my_rectangle = round_rectangle(20, 250, 1300, 2000, radius=20, fill="#1b3857")

        my_rectangle = round_rectangle(50, 300, 1270, 450, radius=20, fill="#2f516f")
        label_1 = Label(canvas,width=15,height=2,text="SERVICES", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(500, 350, anchor="nw", window=label_1)
        btn_non_item_2=Button(canvas,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
        window_btn_non_item_2 = canvas.create_window(750, 350, anchor="nw", window=btn_non_item_2)

        label_1 = Label(canvas,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 500, anchor="nw", window=label_1)

        entry_ser_item_1=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_ser_item_1 = canvas.create_window(55, 530, anchor="nw", height=30,window=entry_ser_item_1)

        label_1 = Label(canvas,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 600, anchor="nw", window=label_1)

        str_ser_item_1 = StringVar()
        entry_ser_iitem_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_ser_item_1)
        str_ser_item_1.set('  Eg: N41554')
        window_entry_ser_iitem_2 = canvas.create_window(55, 630, anchor="nw", height=30,window=entry_ser_iitem_2)

        label_1 = Label(canvas,width=9,height=1,text="SAC Code", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(710, 600, anchor="nw", window=label_1)

        str_ser_iitem_1 = StringVar()
        entry_ser_item_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_ser_iitem_1)
        str_ser_iitem_1.set(' Eg: 998841-Coke and refined petroleum product manufacturing services')
        window_entry_ser_item_2 = canvas.create_window(710, 630, anchor="nw", height=30,window=entry_ser_item_2)


        label_1 = Label(canvas,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(48, 710, anchor="nw", window=label_1)

        comb_ser_item_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_ser_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG-BAGS","BAL-BALE","BDL-BUNDLES","BKL-BUCKLES","BOX-BOX","BOU-BILLIONS OF UNITS","BTL-BOTTLES","BUN-BUNCHES","CAN-CANS","CBM-CUBIC METER","CMS-CENTIMETER","CCM-CUBIC CENTIMETER","CTN-CARTONS","DOZ-DOZEN","DRM-DRUM","GGR-GREAT GROSS","GMS-GRAMS","GRS-GROSS","GYD-GRODD YARDS","KGS-KILOGRAMS","KLR-KILOLITER","KME-KILOMETRE","MTS-METRIC TON","MLT-MILLILITRE","MTR-METERS","NOS-NUMBER","PAC-PACKS","PCS-PIECES","PRS-PAIRS","QTL-QUINTAL","ROL-ROLLS","SQF-SQUARE FEET","SET-SETS","SQM-SQUARE METERS","SQY-SQUARE YARDS","TBS-TABLETS","TGM-TEN GROSS","THD-THOUSAND","TON-TONNES","TUB-TUBES","UGS-US GALLONS","UNT-UNITS","YDS-YARDS","OTH-OTHERS",)
        comb_ser_item_1.current(0)
        window_comb_ser_item_1 = canvas.create_window(55, 740, anchor="nw", width=540, height=30,window=comb_ser_item_1)

        label_1 = Label(canvas,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(705, 710, anchor="nw", window=label_1)

        entry_ser_item_3=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_ser_item_3 = canvas.create_window(710, 740, anchor="nw", height=30,window=entry_ser_item_3)

        canvas.create_line(55, 815, 1260, 815, fill='gray',width=1)


        label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 840, anchor="nw", window=label_1)

        chk_str_ser_item = StringVar()
        chkbtn_ser_item = Checkbutton(canvas, text = "I sell this product/service to my customers.", variable = chk_str_ser_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        window_chkbtn_ser_item = canvas.create_window(55, 870, anchor="nw", window=chkbtn_ser_item)

        label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 940, anchor="nw", window=label_1)

        entry_ser_item_7=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_ser_item_7 = canvas.create_window(55, 970, anchor="nw", height=60,window=entry_ser_item_7)

        label_1 = Label(canvas,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(45, 1070, anchor="nw", window=label_1)
        
        entry_non_item_8=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_non_item_8 = canvas.create_window(55, 1100, anchor="nw", height=30,window=entry_non_item_8)

        chk_str_ser_item_1 = StringVar()
        chkbtn_ser_item_1 = Checkbutton(canvas, text = "Inclusive of tax", variable = chk_str_ser_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn_ser_item_1.select()
        window_chkbtn_ser_item_1 = canvas.create_window(55, 1135, anchor="nw", window=chkbtn_ser_item_1)

        label_1 = Label(canvas,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(703, 1070, anchor="nw", window=label_1)

        comb_ser_item_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_ser_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
        comb_ser_item_3.current(0)
        window_comb_ser_item_3 = canvas.create_window(710, 1100, anchor="nw", width=540, height=30,window=comb_ser_item_3)

        label_1 = Label(canvas,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(41, 1180, anchor="nw", window=label_1)

        
        comb_ser_item_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_ser_item_6['values'] = ("Choose...","Billable Expense income","Product Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discounts","Sales of Product Income","Cost of sales","Equipment Rental for Jobs","Uncategorised Income","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Internet Expenses","Meals and Enetrtainments","Office Suppliers","Postage and Delivery","Printing and Reprooduction","Professional Fees","Purchases","Rent Expense","Repair and Maintananace","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities","Finance charge Income","Insurance Proceeds Received","Interest Income","Proceeds From Sale os Assets","Shipping and delivery Income","Ask My Accountant","CGST Write-off","GST Write-off","IGST Write-off","Miscellaneous Expense","Political Contributions","Reconcilation Discrepancies","SGST Write-off","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",)
        comb_ser_item_6.current(0)
        window_comb_ser_item_6 = canvas.create_window(55, 1210, anchor="nw", width=330, height=30,window=comb_ser_item_6)

        income_ser_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
        window_income_ser_btn = canvas.create_window(395, 1210, anchor="nw", window=income_ser_btn)

        label_1 = Label(canvas,width=10,height=1,text="Abatement %", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(522 , 1180, anchor="nw", window=label_1)

        str_ser_iitem_2 = StringVar()
        entry_ser_iitem_11=Entry(canvas,width=50,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_ser_iitem_2)
        str_ser_iitem_2.set(' 0')
        window_entry_ser_iitem_11 = canvas.create_window(520, 1210, anchor="nw", height=30,window=entry_ser_iitem_11)

        label_1 = Label(canvas,width=15,height=1,text="Service Type", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(877, 1180, anchor="nw", window=label_1)

        comb_ser_iitem_7 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_ser_iitem_7['values'] = ("Choose...",)
        comb_ser_iitem_7.current(0)
        window_comb_ser_iitem_7 = canvas.create_window(900, 1210, anchor="nw", width=345, height=30,window=comb_ser_iitem_7)

        canvas.create_line(55, 1275, 1260, 1275, fill='gray',width=1)

        label_1 = Label(canvas,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(26, 1300, anchor="nw", window=label_1)

        chk_str_ser_pitem = StringVar()
        chkbtn_ser_pitem = Checkbutton(canvas, text = "I Purchase this product/service from Supplier.", variable = chk_str_ser_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        window_chkbtn_ser_pitem = canvas.create_window(55, 1330, anchor="nw", window=chkbtn_ser_pitem)


        label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(51, 1400, anchor="nw", window=label_1)

        entry_ser_item_9=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_ser_item_9 = canvas.create_window(55, 1430, anchor="nw", height=60,window=entry_ser_item_9)

        label_1 = Label(canvas,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(50, 1530, anchor="nw", window=label_1)
        
        entry_ser_item_10=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_ser_item_10 = canvas.create_window(55, 1560, anchor="nw", height=30,window=entry_ser_item_10)

        chk_str_sser_item_2 = StringVar()
        chkbtn_sser_item_2 = Checkbutton(canvas, text = "Inclusive of Tax", variable = chk_str_sser_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn_sser_item_2.select()
        window_chkbtn_sser_item_2 = canvas.create_window(55, 1600, anchor="nw", window=chkbtn_sser_item_2)

        label_1 = Label(canvas,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(700, 1530, anchor="nw", window=label_1)

        comb_ser_item_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_ser_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
        comb_ser_item_5.current(0)
        window_comb_ser_item_5 = canvas.create_window(710, 1565, anchor="nw", width=540, height=30,window=comb_ser_item_5)

        label_1 = Label(canvas,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(47, 1660, anchor="nw", window=label_1)

        comb_ser_item_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_ser_item_6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
        comb_ser_item_6.current(0)
        window_comb_ser_item_6 = canvas.create_window(55, 1690, anchor="nw", width=330, height=30,window=comb_ser_item_6)

        expense_ser_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
        window_expense_ser_btn = canvas.create_window(395, 1690, anchor="nw", window=expense_ser_btn)

        label_1 = Label(canvas,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(520, 1660, anchor="nw", window=label_1)

        str_sser_iitem_2 = StringVar()
        entry_sser_item_11=Entry(canvas,width=50,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_sser_iitem_2)
        str_sser_iitem_2.set(' 0')
        window_entry_sser_item_11 = canvas.create_window(520, 1690, anchor="nw", height=30,window=entry_sser_item_11)

        label_1 = Label(canvas,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(897, 1660, anchor="nw", window=label_1)

        comb_ser_item_7 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_ser_item_7['values'] = ("Select Supplier",)
        comb_ser_item_7.current(0)
        window_comb_ser_item_7 = canvas.create_window(900, 1690, anchor="nw", width=345, height=30,window=comb_ser_item_7)

        ser_sub_btn1=Button(canvas,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
        window_ser_sub_btn1 = canvas.create_window(575, 1800, anchor="nw", window=ser_sub_btn1)

    btn_3=Button(canvas,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=ser_add_item)
    window_btn_3 = canvas.create_window(330, 770, anchor="nw", window=btn_3)

    my_rectangle = round_rectangle(700, 600, 1150, 850, radius=20, fill="#2f516f")

    label_1 = Label(canvas,width=10,height=1,text="Bundle", font=('arial 20'),background="#2f516f",fg="white") 
    window_label_1 = canvas.create_window(845, 650, anchor="nw", window=label_1)

    label_1 = Label(canvas,width=46,height=2,text="A bundle is a group of software programs or hardware \ndevices that are grouped together and sold as one.", font=('arial 12'),background="#2f516f",fg="white") 
    window_label_1 = canvas.create_window(720, 700, anchor="nw", window=label_1)

    btn_4=Button(canvas,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12')
    window_btn_4 = canvas.create_window(830, 770, anchor="nw", window=btn_4)


btn1=Button(text='Add Products', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_product)
window_btn1 = canvas.create_window(1050, 430, anchor="nw", window=btn1)

# run the application
root.mainloop()