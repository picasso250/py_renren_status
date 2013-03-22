
from tkinter import *

root = Tk()
root.title('xz')

status_var = StringVar()
entry = Entry(root, textvariable=status_var)
entry.pack(side=LEFT)

def update_status():
    status_text = status_var.get()

button = Button(root, text='发布状态', command=update_status)
button.pack(side=RIGHT)

root.mainloop()
