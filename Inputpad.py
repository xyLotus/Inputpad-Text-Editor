import tkinter as tk
from tkinter import *

file_opened = False

def save_file_init():
    global file_save_name
    file_save_name = e2.get()
    file_2 = open(file_save_name, "w")

    file_2.write(myText_Box.get("1.0",'end-1c'))


def save_file():
    global e2
    if file_opened == True:
        print("Saving...")
        f = open(file_name, "w")
        f.write(myText_Box.get("1.0",'end-1c'))
    else:
        root_3 = tk.Tk()

        root_3.title("inputpad - Save File")
        root_3.geometry("200x150")
        root_3.resizable(False, False)

        l2 = Label(root_3, text="Save File: ", font="sans-serif 10")
        l2.place(x=10,y=10)

        e2 = Entry(root_3, font="sans-serif 10")
        e2.place(x=10,y=50)

        b2 = Button(root_3, text="Save File", command=save_file_init, font="sans-serif 10")
        b2.place(x=10,y=90)

def delete_open_file_window():
    root_2.destroy()

def clear_input():
    myText_Box.replace("1.0",'end-1c',"")

def get_input():
    global file, file_name
    global content, file_opened

    file_name = e1.get()
    file = open(file_name, "r")

    myText_Box.insert(END, file.read())

    root.title("inputpad - " + str(e1.get()))
    file_opened = True
    delete_open_file_window()

def open_file():
    global file_name, e1, root_2

    root_2 = tk.Tk()

    root_2.geometry("200x150")
    root_2.title("inputpad - Open")
    root_2.resizable(False, False)

    l1 = Label(root_2, font="sans-serif 10", text="File Name: ")
    l1.place(x=30,y=10)

    e1 = Entry(root_2, font="sans-serif 10")
    e1.place(x=30,y=50)

    b1 = Button(root_2,text="Open File", font="sans-serif 10", command=get_input)
    b1.place(x=30,y=100)


root = tk.Tk()

root.title("inputpad - by Lotus - Private Edition")
root.geometry("513x515")
root.resizable(False, False)

myText_Box = Text(font="sans-serif 20",width=30,height=15.51,bg="white")
myText_Box.place(x=60,y=0)

Button(text="save", command=save_file, height=2, width=5).place(x=10,y=10)
Button(text="Open", command=open_file, height=2, width=5).place(x=10,y=50)
Button(text="clear", command=clear_input, height=2, width=5).place(x=10,y=90)

root.mainloop()
