# coding=utf8

from tkinter import *
import threading
import renren_api

root = Tk()
root.title('状态帝师')

status_var = StringVar()
entry = Entry(root, textvariable = status_var)
entry.pack(side = LEFT)

def update_status():
    btn.config(state = DISABLED, text = btn_text_dict['busy'])
    threading.Thread(target = do_update, args = (), name = 'update thread').start()

def do_update():
    status_text = status_var.get()
    token = renren_api.parse_token('http://xctest.sinaapp.com/renren_oauth#access_token=171902%7C6.e337de58f8715af0b7738ed90876a4d9.2592000.1366473600-228417767&expires_in=2595103&scope=status_update')
    if renren_api.update_status(token['access_token'], status_text):
        status_var.set('')
    btn.config(state = NORMAL, text = btn_text_dict['normal'])

btn_text_dict = {
    'normal': '发布状态',
    'busy': '正在发布'
}
btn = Button(root, text = btn_text_dict['normal'], command = update_status)
btn.pack(side = RIGHT)

root.mainloop()
