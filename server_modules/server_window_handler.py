import socket
from constants.network_constants import *
import thread
from server_modules.client_modules_for_server import start_judge
from server_modules.start_server_module import startServer
import tkMessageBox

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

total_problems = 0
q = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class MainWindow(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        self.s = s
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Add Problems for Contest", 
                                command=self.create_window)
        self.button.pack()

        self.button = tk.Button(self, text="Start Server", 
                                command=lambda: startServer(total_problems , q , s))
        self.button.pack()

    def create_window(self):
        problem_add_window = tk.Toplevel(self)
        problem_add_window.wm_title('Add problems For Contest')
        labelText = tk.StringVar()
        labelText.set('Enter Problem Name')
        label1 = tk.Label(problem_add_window, textvariable=labelText, height=1)
        label1.pack()

        problem_name = tk.Text(problem_add_window, height=1, width=30)
        problem_name.pack()
        problem_name.insert(tk.END, "")

        labelText = tk.StringVar()
        labelText.set('Enter Problem Code')
        label1 = tk.Label(problem_add_window, textvariable=labelText, height=1)
        label1.pack()

        problem_code = tk.Text(problem_add_window, height=1, width=30)
        problem_code.pack()
        problem_code.insert(tk.END, "")

        button = tk.Button(problem_add_window, text="Add", command=lambda: addProblem(problem_name , problem_code , problem_add_window))
        button.pack()



def addProblem(problem_name , problem_code , problem_add_window):
    global total_problems
    global q
    
    total_problems = total_problems + 1
    
    print problem_name.get("1.0",tk.END) + '$%$' + problem_code.get("1.0",tk.END)
    q.append(str(total_problems) + '.)' + problem_name.get("1.0",tk.END) + '$%$' + problem_code.get("1.0",tk.END))
    tkMessageBox.showinfo('Info', 'Problem Successfully Added To Contest!!')
    problem_add_window.destroy
    
