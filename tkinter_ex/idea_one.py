from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title = "Tkinter Filedialog"
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text="Open File")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)
        self.button()

    def button(self):
        self.button = ttk.Button(self.labelFrame, text="Browse a file", command=self.file_dialog)
        self.button.grid(column=1, row=1)

    def file_dialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/")
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)


root = Root()
root.mainloop()
