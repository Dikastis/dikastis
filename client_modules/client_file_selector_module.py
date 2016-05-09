import tkFileDialog
import tkMessageBox

def select(var,soc):
	global selected_sol_file_path
	problem_selected = var.get()
	problem_selected = problem_selected.split(' -- ')[0]
	# opening file selector window
	file_path_string = tkFileDialog.askopenfilename(filetypes = (("C Files", "*.c")
                                                         ,("C++ Files", "*.cpp")))

	selected_sol_file_path = file_path_string
	print selected_sol_file_path

	file = open(selected_sol_file_path,'r')
	data = file.read()
	print data
	sol_data = data

	#sending problem name
	soc.send(problem_selected)
	response = soc.recv(100)
	print response
	soc.send(data)

	response = soc.recv(100)
	print response #3002


	# result = soc.recv(100)
	# tkMessageBox.showinfo('report', 'submission result : ' + result)
	# print result

