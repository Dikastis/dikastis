import socket
from constants.network_constants import *
from constants.file_constants import *
import thread
from server_modules.client_modules_for_server import start_judge
from server_modules.start_server_module import startServer
import tkMessageBox
import ttk
import tkFileDialog
from server_modules.data_extractor import *

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

total_problems = 0
q = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
input_file_path_string = ''
output_file_path_string = ''
statement_file_path = ''
class MainWindow(tk.Frame):
  

    def __init__(self, *args, **kwargs):
        self.s = s

        def problem_window(self):
            global q, s
            def focus_next_window(event):
                event.widget.tk_focusNext().focus()
                return("break")

            def file_loader(type):
                global input_file_path_string, output_file_path_string,statement_file_path

                if type == "in":
                    input_file_path_string = tkFileDialog.askopenfilename(filetypes = (("Input Files", "*.in")
                                                                                        ,("txt Files", "*.txt")))
                elif type == "out":
                    output_file_path_string = tkFileDialog.askopenfilename(filetypes = (("Output Files", "*.out")
                                                                                        ,("txt Files", "*.txt")))
                elif type == "statement":
                    statement_file_path = tkFileDialog.askopenfilename(filetypes = (("Statement File", "*.txt")
                                                                                    ,("All Files", "*.*")))

            labelText = tk.StringVar()
            labelText.set('Enter Problem name')
            label1 = tk.Label(self, textvariable=labelText, height=1)
            label1.grid(row=1,column=0)

            problem_name = tk.Text(self, height=1, width=30)
            problem_name.grid(row=1,column=1)
            problem_name.insert(tk.END, "")
            
            problem_name.bind("<Tab>", focus_next_window)

            labelText = tk.StringVar()
            labelText.set('Enter Problem Code')
            label1 = tk.Label(self, textvariable=labelText, height=1)
            label1.grid(row=2,column=0)

            problem_code = tk.Text(self, height=1, width=30)
            problem_code.grid(row=2,column=1)
            problem_code.insert(tk.END, "")

            problem_code.bind("<Tab>", focus_next_window)

            button = tk.Button(self,  text="Input file", command=lambda:file_loader("in"))
            button.grid(row=3,column=1)
            button = tk.Button(self, text="Output file",command=lambda:file_loader("out"))
            button.grid(row=3,column=2)
            button = tk.Button(self, text="Problem Statement",command=lambda:file_loader("statement"))
            button.grid(row=4,column=1)
            


            button = tk.Button(self, text="Click To ADD", command=lambda: addProblem(problem_name , problem_code , listbox))
            button.grid(row=5,column=1)
            button = tk.Button(self, text="startServer",command=lambda:startServer(total_problems,q,s))
            button.grid(row=6,column=1)

            listbox = tk.Listbox(self,width=60)
            listbox.grid(row=7,column=1)
            listbox.insert(tk.END, "problems:")

            i = 0
            data = get_problem_data("1")
            for i in range(len(data)):
                item = 'name: ' + data[i].problem_name + ' | code: ' + data[i].problem_code + ' | input_file: ' + str(data[i].problem_name+data[i].problem_code) + ".in" + ' | out_file:' + str(data[i].problem_name+data[i].problem_code) + ".out"
                listbox.insert(tk.END,item)


        tk.Frame.__init__(self, *args, **kwargs)
        tk.Frame(self,width=600,height=400)
        
        notebook = ttk.Notebook(self)
        notebook.grid(row=0)
        subframe = tk.Frame(self,width=280,height=400)
        subframe.grid(row=0,column=0)
        notebook.add(subframe, text="ADD Problems", state="normal")
        problem_window(subframe)
        
        subframe1 = tk.Frame(self,width=280,height=400)
        subframe1.grid(row=0,column=1)
        notebook.add(subframe1, text="All Submission List", state="normal")
        
        subframe21 = tk.Frame(self,width=280,height=400)
        subframe21.grid(row=0,column=2)
        notebook.add(subframe21, text="Broadcast", state="normal")


def addProblem(problem_name , problem_code, listbox):
        global total_problems
        global q

        total_problems = total_problems + 1
        name = problem_name.get("1.0",tk.END)[:-1]
        code = problem_code.get("1.0",tk.END)[:-1]

        in_file = open(input_file_path_string,'r')
        data = in_file.read()
        server_in_file_path = file_path + str(name+code) + ".in"
        server_in_file = open(server_in_file_path,'w')
        server_in_file.write(data)

        out_file = open(output_file_path_string,'r')
        data = out_file.read()
        server_out_file_path = file_path + str(name+code) + ".out"
        server_out_file = open(server_out_file_path,'w')
        server_out_file.write(data)
       
        statement_file = open(statement_file_path,'r')
        statement_data = statement_file.read()

        data = problems_data()
        data.problem_code = code
        data.problem_name = name
        data.problem_statement = statement_data
        add_problem_data(data)

        item = 'name: ' + name + ' | code: ' + code + ' | input_file: ' + str(name+code) + ".in" + ' | out_file:' + str(name+code) + ".out"
        listbox.insert(tk.END,item)


        # print name + '$%$' + code
        q.append(str(total_problems) + '.)' + name + '$%$' + code)


        tkMessageBox.showinfo('Info', 'Problem Successfully Added To Contest!!')
        problem_name.delete('1.0', tk.END)
        problem_code.delete('1.0', tk.END)
