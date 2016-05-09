import socket
from constants.network_constants import *
from client_modules.client_file_selector_module import select
import models
from constants.color_constants import *
import sys
import tkMessageBox
import tkFont
import ttk
import ScrolledText
import thread
import pickle
import ttk
import os

sol_data = ''
problem_selected = ''

HOST = ''
#Host = ''
PORT = 4466



soc = socket.socket()
soc.connect((HOST , PORT))
soc.send('1000') # 10 refres to client type 
response = soc.recv(1000)

if response == "3001":
    pass
else:
    #handle error
    pass





try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def start_cliet_reciever(ok):
    os.system('python client_reciever.py')

   
def setNotifications(list):
    list.delete(1,tk.END)
    f = open('notifications.txt','r')
    notification_list = f.read().splitlines()
    for notification in notification_list:
        print notification
        if notification != "":
            list.insert(tk.END, notification.split('$$$')[0] + " : " + notification.split('$$$')[1])



def start(soc):
    soc.send('3001')
    data = soc.recv(100000)
    f = open('dd.b','w')
    f.write(data)
    f.close()

    problem_data = pickle.load(open('dd.b','rb'))

    choices = []

    for problem in problem_data:
        choice = problem.problem_code + " -- " + problem.problem_name
        choices.append(choice)



    root = tk.Tk() # create a top-level window
    master = tk.Frame(root, name='master') # create Frame in "root"
    master.pack(fill=tk.BOTH) # fill both sides of the parent

    root.title('Dikastis Client') # title for top-level window
    # quit if the window is deleted
    root.protocol("WM_DELETE_WINDOW", master.quit)

    nb = ttk.Notebook(master, name='nb') # create Notebook in "master"
    nb.pack(fill=tk.BOTH, padx=2, pady=3) # fill "master" but pad sides

    # create each Notebook tab in a Frame
    master_submit = tk.Frame(nb, name='master-submit')
    tk.Label(master_submit, text="Code Submission").pack(fill=tk.BOTH , expand = True)

    # breaking line
    labelText = tk.StringVar()
    labelText.set('\n')
    label1 = tk.Label(master_submit, textvariable=labelText, height=1)
    label1.pack()
    
    var = tk.StringVar(master_submit)
    # initial value
    var.set('select problem')
    option = tk.OptionMenu(master_submit, var, *choices)
    option.pack(pady = 1 , side='left')
    button = tk.Button(master_submit, text="browse file & submit", command=lambda: select(var,soc))
    button.pack(side='left', padx=20, pady=1)

    labelText = tk.StringVar()
    labelText.set('\n')
    label1 = tk.Label(master_submit, textvariable=labelText, height=1)
    label1.pack()

    nb.add(master_submit, text="submit code") # add tab to Notebook

    # repeat for each tab
    notification_tab = tk.Frame(master, name='master-bar')
    btn = tk.Button(notification_tab, text="refresh", command = lambda: setNotifications(listbox))
    btn.pack(fill=tk.BOTH , expand = True , side = 'top')

    listbox = tk.Listbox(notification_tab , width=100)
    listbox.pack()
    listbox.insert(tk.END, "Notifications :")

    nb.add(notification_tab, text="notifications")

    root.mainloop()




def authenticate(username , password):
    soc.send( str( username.get()) + " " + str(password.get()) ) 
    result = soc.recv(100)
    if result == "200": # 200 code refers that login was successful

        #saving username
        f=open('login_id.txt','w')
        f.write( str( username.get() ))
        f.close()
        
        login_window.destroy()
        thread.start_new_thread(start_cliet_reciever,("ok",))
        #os.system('python client_reciever.py')
        start(soc)
    else:# 201 for wrong
        tkMessageBox.showinfo("alert", "Wrong id/password combination !!")
        pass



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







