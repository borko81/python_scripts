from tkinter import *
from tkinter import messagebox

print(messagebox)
top = Tk()
top.geometry("200x100")


def message():
    v = checkvar.get()
    messagebox.showinfo("Hello", "This is from {}".format(v))

labelframe = LabelFrame(top, text="Label frame")
checkvar = StringVar()

ch1 = Radiobutton(top, text="C", variable=checkvar, value='C')
ch1.pack()
ch2 = Radiobutton(top, text='B', variable=checkvar, value='B')
ch2.pack()

labelframe.pack(fill="both", expand="yes")



b = Button(top, text="Simple", command=message, fg='pink', bg='black')
b.pack()

label = Label(top,text='TExt from end')
label.pack()

top.mainloop()
