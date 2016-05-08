import socket
from constants.network_constants import *
import thread
from server_modules.client_modules_for_server import start_judge
from server_modules.start_server_module import startServer
import tkMessageBox
import ttk
import tkFileDialog
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

            def file_loader(type):
                if type == "in":
                    input_file_path_string = tkFileDialog.askopenfilename(filetypes = (("Input Files", "*.in")
                                                                                        ,("txt Files", "*.txt")))
                elif type == "out":
                    output_file_path_string = tkFileDialog.askopenfilename(filetypes = (("Output Files", "*.out")
                                                         ,("txt Files", "*.txt")))
            labelText = tk.StringVar()
            labelText.set('Enter Problem name')
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

            button = tk.Button(self, text="Input file", command=lambda:file_loader("in"))
            button.pack()
            button = tk.Button(self, text="Output file",command=lambda:file_loader("out"))
            button.pack()

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
        name = problem_name.get("1.0",tk.END)[:-1]
        code = problem_code.get("1.0",tk.END)[:-1]

        item = 'name: ' + name + ' code: ' + code
        listbox.insert(tk.END,item)
        
        print name + '$%$' + code
        q.append(str(total_problems) + '.)' + name + '$%$' + code)
        tkMessageBox.showinfo('Info', 'Problem Successfully Added To Contest!!')

        problem_name.delete('1.0', tk.END)
        problem_code.delete('1.0', tk.END)
        

