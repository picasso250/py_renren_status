# coding=utf8

from tkinter import *
import threading
import renren_api
import webbrowser

# config
token_file = 'renren.token'
btn_text_dict = {
    'normal': '发布状态',
    'busy': '正在发布',
    'save_token': '保存令牌'
}

# ui
root = Tk()
root.title('状态帝师')

status_var = StringVar()
entry = Entry(root, textvariable = status_var)
btn = Button(root, text = btn_text_dict['normal'], command = update_status)
entry.pack(side = LEFT)
btn.pack(side = RIGHT)

root.mainloop()

# events

def update_status():
    btn.config(state = DISABLED, text = btn_text_dict['busy'])
    threading.Thread(target = do_update, args = (), name = 'update thread').start()

def do_update():
    status_text = status_var.get()

    try:
        f = open(token_file, 'r')
    except IOError:
        auth_url = renren_api.get_auth_url()
        webbrowser.open_new(auth_url)
        btn.config(state = NORMAL, text = btn_text_dict['save_token'], command = save_token)
        return

    url = f.read()
    f.close()
    token = renren_api.parse_token(url)
    if renren_api.update_status(token['access_token'], status_text):
        status_var.set('')
    btn.config(state = NORMAL, text = btn_text_dict['normal'])

def save_token():
    url = status_var.get()
    f = open(token_file, 'w')
    f.write(url)
    f.close()
    btn.config(text = btn_text_dict['normal'], command = update_status)