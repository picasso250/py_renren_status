
from tkinter import *
import renren_api

root = Tk()
root.title('xz')

status_var = StringVar()
entry = Entry(root, textvariable=status_var)
entry.pack(side=LEFT)

def update_status():
    status_text = status_var.get()
    token = renren_api.parse_token('http://xctest.sinaapp.com/renren_oauth#access_token=171902%7C6.e337de58f8715af0b7738ed90876a4d9.2592000.1366473600-228417767&expires_in=2595103&scope=status_update')
    r = renren_api.update_status(token['access_token'], status_text)
    print(r)

button = Button(root, text='发布状态', command=update_status)
button.pack(side=RIGHT)

root.mainloop()
