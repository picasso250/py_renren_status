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
    f = open('renren.token', 'r')
    url = f.read()
    f.close()
    token = renren_api.parse_token(url)
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
