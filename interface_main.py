from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def wipe_frame():
    for widget in frm.winfo_children():
        widget.destroy()


def login_screen():
    wipe_frame()
    image = Image.open("ccclogo.png")
    image = image.resize((200, 100))
    ttk.Entry(frm).grid(column=0, row=2)
    img = ImageTk.PhotoImage(image)
    ttk.Label(root, image=img).grid(column=1,row=1)
    ttk.Label(frm,text='Enter your password:',font='Arial').grid(column=0,row=1)



def second_screen():
    wipe_frame()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Back", command=main_screen).grid(column=1, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)


def main_screen():
    for widget in frm.winfo_children():
        widget.destroy()
    ttk.Label(frm, text="Hello World!").grid(column=7, row=10)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=3)
    ttk.Button(frm, text="OtherScreen", command=second_screen).grid(column=4, row=4)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
login_screen()
root.mainloop()
