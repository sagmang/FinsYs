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
    label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(480, 85, anchor="nw", window=label_1)
    canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

    my_rectangle = round_rectangle(20, 250, 1300, 1535, radius=20, fill="#1b3857")

    # def change(event):
    #     my_rectangle = round_rectangle(200, 300, 650, 550, radius=20, fill="grey")
    #     label_1 = Label(canvas,width=5,height=1,text="Hello", font=('arial 20'),background="#1b3857",fg="white") 
    #     window_label_1 = canvas.create_window(375, 350, anchor="nw", window=label_1)

    
    # #my_rectangle = round_rectangle(200, 300, 650, 550, radius=20, fill="grey")

    # image_2 = Image.open("images/lowstock.png")
    # resize_image = image_2.resize((90,90))
    # image_2 = ImageTk.PhotoImage(resize_image)
    # btlogo_2 = Label(canvas, width=90, height=90, background="#1b3857", image = image_2) 
    # window_image = canvas.create_window(375,380, anchor="nw", window=btlogo_2)
    # btlogo_2.photo = image_2

    # btlogo_2.bind("<Enter>", change)


btn1=Button(text='Add Products', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_product)
window_btn1 = canvas.create_window(1050, 430, anchor="nw", window=btn1)

# run the application
root.mainloop()