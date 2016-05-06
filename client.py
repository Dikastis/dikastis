import socket
from constants.network_constants import *
from client_modules.client_file_selector_module import select

sol_data = ''
problem_selected = ''

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

'''loading list of questions'''
soc = socket.socket()
soc.connect(('',PORT))
data = soc.recv(10000)
soc.send('problems recieved')
choices = data.split('&&&')

print soc.recv(100)

root = tk.Tk()
root.title("Code Judge Client")

var = tk.StringVar(root)
# initial value
var.set('select problem')
option = tk.OptionMenu(root, var, *choices)
option.pack(pady = 1 , side='left')
button = tk.Button(root, text="browse file & submit", command=lambda: select(var,soc))
button.pack(side='left', padx=20, pady=1)

labelText = tk.StringVar()
labelText.set('\n')
label1 = tk.Label(root, textvariable=labelText, height=10)
label1.pack()
root.mainloop()

