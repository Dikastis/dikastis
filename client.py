import socket
from constants.network_constants import *
from client_modules.client_file_selector_module import select
from constants.color_constants import *
import sys
import tkMessageBox
import tkFont

sol_data = ''
problem_selected = ''

'''loading list of questions'''
#soc = socket.socket()
#soc.connect(('',PORT))

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def __start():

    data = "asdfghjkljhgfd$cvkz$xdghjkjhcx$hjklkjhgf";
    choices = data.split('$')

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

def __authenticate(username , password):
    #soc.send( str(username.get()) + str(password.get()) ) 
    #result = soc.recv(100)
    result = "asdflkjh34789ccy78okcdr56ujmnbvf"
    if result != "wrong":
        login_window.destroy()
        start()
    else:
        pass
        #wrong id pw



class Login:
    def __init__(self,parent):
        self.window = parent

    def show(instance): 
        window = tk.Toplevel()
        frame = tk.Frame(window,bg=backColor)
        menubar = tk.Menu(window)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command="sys.exit()")
        menubar.add_cascade(label="File", menu=filemenu)
        window.config(menu=menubar)
        
        label2 = tk.Label(frame, text = "Username", fg="Black", bg=backColor)
        label3 = tk.Label(frame, text = "Password", fg="Black", bg=backColor)
        login_userid = tk.Entry(frame,bg=outFocusColor)
        login_passwd = tk.Entry(frame,bg=outFocusColor,show="*")
        login_userid.bind("<Return>", login_passwd.focus_set())
        btnLogin = tk.Button(frame, text="Login", command= lambda: authenticate( login_userid , login_passwd ) )

        frame.title = "Dikastis Login" 
        frame.grid()
        label2.grid(row=2, column=0,columnspan=3, sticky=tk.W)
        login_userid.grid(row=2, column=6, columnspan=5,sticky=tk.W)
        label3.grid(row=3, column=0,columnspan=3, sticky=tk.W)
        login_passwd.grid(row=3, column=6, columnspan=5,sticky=tk.W)
        btnLogin.grid(row=4, column=4, sticky=tk.W)


#showing login screen
login_window = tk.Tk()
login_window.withdraw()
login_window.title("Dikastis Login")
login_views = Login(login_window)
login_views.show()

login_window.mainloop()

