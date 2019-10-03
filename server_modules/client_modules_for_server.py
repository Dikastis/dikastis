from soldier import soldier

submission_queue = []

def start_judge(conn):
	# ls = []        
	# name = []
	name = conn.recv(100)
	
	# print sol_recieved_for_problem
	# ls=split(sol_recieved_for_problem,')')
	# print ls
	# name=split(ls[1],'\n')
	print name

	# print 
	conn.send('name recieved')

	sol = conn.recv(1000)
	print sol
	f=open('/home/tanmay/Documents/Dikastis/minor/dikastis/submissions/test.cpp','w');
	f.write(sol)
	f.close()
	f=open('/home/judge/test.cpp','w');
	f.write(sol)
	f.close()
	conn.send('sol recieved')

	response = conn.recv(100)
	print response

	# sending result of submission
	a=soldier.run("python checker.py "+"test "+name)
	print a.output
	conn.send(a.output)

	start_judge(conn)
