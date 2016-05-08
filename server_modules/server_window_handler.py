import socket
from constants.network_constants import *
import thread
from server_modules.client_modules_for_server import start_judge
from server_modules.start_server_module import startServer
import tkMessageBox
import ttk
# from server_modules.database import *

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
        

        def problem_window(self):
            def focus_next_window(event):
                event.widget.tk_focusNext().focus()
                return("break")

            labelText = tk.StringVar()
            labelText.set('Enter Problem Name')
            label1 = tk.Label(self, textvariable=labelText, height=1)
            label1.pack()

            problem_name = tk.Text(self, height=1, width=30)
            problem_name.pack()
            problem_name.insert(tk.END, "")
            
            problem_name.bind("<Tab>", focus_next_window)

            labelText = tk.StringVar()
            labelText.set('Enter Problem Code')
            label1 = tk.Label(self, textvariable=labelText, height=1)
            label1.pack()

            problem_code = tk.Text(self, height=1, width=30)
            problem_code.pack()
            problem_code.insert(tk.END, "")

            problem_code.bind("<Tab>", focus_next_window)

            button = tk.Button(self, text="Add", command=lambda: addProblem(problem_name , problem_code , listbox))
            button.pack()

            listbox = tk.Listbox(self,width=30)
            listbox.pack()
            listbox.insert(tk.END, "problems:")



        tk.Frame.__init__(self, *args, **kwargs)
        tk.Frame(self,width=600,height=400)
        
        notebook = ttk.Notebook(self)
        notebook.pack()
        subframe = tk.Frame(self,width=280,height=400)
        subframe.pack()
        notebook.add(subframe, text="ADD Problems", state="normal")
        problem_window(subframe)
        
        subframe1 = tk.Frame(self,width=280,height=400)
        subframe1.pack()
        notebook.add(subframe1, text="All Problem List", state="normal")
        
        subframe21 = tk.Frame(self,width=280,height=400)
        subframe21.pack()
        notebook.add(subframe21, text="Broadcast", state="normal")


def addProblem(problem_name , problem_code, listbox):
        global total_problems
        global q

        total_problems = total_problems + 1
        item = 'name: ' + problem_name.get("1.0",tk.END) + ' code: ' + problem_code.get("1.0",tk.END)
        listbox.insert(tk.END,item)
        print problem_name.get("1.0",tk.END) + '$%$' + problem_code.get("1.0",tk.END)
        q.append(str(total_problems) + '.)' + problem_name.get("1.0",tk.END) + '$%$' + problem_code.get("1.0",tk.END))
        tkMessageBox.showinfo('Info', 'Problem Successfully Added To Contest!!')
        problem_name.delete('1.0', tk.END)
        problem_code.delete('1.0', tk.END)
        

