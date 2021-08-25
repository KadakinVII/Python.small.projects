from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msbx
from tkinter import filedialog as fild

# Functions working with files
def clear():
    warn = 'Are you sure? All information will be deleted!'
    answer = msbx.askyesno(title = 'Warning', message = warn)
    if answer:
        text.delete(1.0, END)
def read():
    warn = 'Are you sure? All information will be deleted!'
    answer = msbx.askyesno(title = 'Warning', message = warn)
    if answer:
        fileName = fild.askopenfilename(
            filetypes = (('TXT files', '*.txt'), ('Python files', '*.py'), ('Python Windowed files', '*.pyw'), ('All files', '*.*')))
        file = open(fileName, mode = 'r+', encoding = 'utf-8')
        text.delete(1.0, END)
        text.insert(1.0, file.read())
def save():
    answer = msbx.askyesno(title = 'Warning', message = 'Are you sure?')
    if answer:
        fileName = fild.asksaveasfilename(
                filetypes = (('TXT files', '*.txt'), ('Python files', '*.py'), ('Python WIndowed files', '*.pyw'), ('All files', '*.*')))
        file = open(fileName, mode = 'w', encoding = 'utf-8')
        file.write(text.get(1.0, END))
        file.close()
def close():
    warn = 'Are you sure? All information will be deleted!'
    answer = msbx.askyesno(title = 'Warning', message = warn)
    if answer:
        root.destroy()
        exit()
def font():
    def insertfont(event):
        size = sizebox.get()
        index = fontbox.curselection()
        font = fontbox.get(index)
        text.config(font = font + '' + size)
        win.destroy()
    win = Toplevel()
    win.title('Fonts')
    fontbox = Listbox(win)
    sizebox = Spinbox(win, from_ = 8, to = 72)
    fontlist = ['Arial', 'Calibri', 'Courier', 'Fixedsys', 'Segoe', 'System', 'Tahoma', 'Times', 'Verdana']
    fontbox.bind('<Double-Button-1>', insertfont)
    win.bind('<Return>', insertfont)
    fontbox.pack(fill = X)
    sizebox.pack()
    for font in fontlist:
        fontbox.insert(END, font)
    sizebox.insert(0, '10')
def helper():
    win = Toplevel()
    name = Label(win, text = 'Tk Lite Text Editor', font = 'Segoe 48')
    ver = Label(win, text = 'Pre-release 3', font = 'Segoe 16')
    name.pack()
    ver.pack()

# Interface programming
root = Tk()
root.title('Tk LTE Pre-release 3')
text = Text()
scroller = Scrollbar(command = text.yview)
text.config(yscrollcommand = scroller.set)
mainmenu = Menu(root)
root.config(menu=mainmenu)

fil = Menu(mainmenu, tearoff = 0)
fil.add_command(label = 'Open', command = read)
fil.add_command(label = 'Save', command = save)
fil.add_command(label = 'New', command = clear)
fil.add_command(label = 'Quit', command = close)
mainmenu.add_cascade(label = 'File', menu = fil)

form = Menu(mainmenu, tearoff = 0)
form.add_command(label = 'Font', command = font)
mainmenu.add_cascade(label = 'Format', menu = form)

hlp = Menu(mainmenu, tearoff = 0)
hlp.add_command(label = 'About', command = helper)
mainmenu.add_cascade(label = 'Help', menu = hlp)

# Window Mainloop
scroller.pack(side = RIGHT, fill = Y, anchor = NW)
text.pack(side = RIGHT, fill = BOTH)
root.mainloop()

