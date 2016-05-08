from models import *
from data_extractor import *
import socket
import pickle 

"""
data = client_data()
data.team_id = "test126"
data.team_name = "test test"
data.problem_code = "q1"
data.language = "C++"
#data.timestamp = 1462698376
file = open("data.txt","r")
data.filename = file.read()
data.submission_number = 1

add_client_details(data) """

data = problems_data()
data.problem_code = "q1"
data.problem_name = "testing problem"
data.problem_statement = "this is a testing problem.Here you can test your problem"

data2 = problems_data()
data2.problem_code = "q2"
data2.problem_name = "testing problem2"
data2.problem_statement = "this is a testing problem.Here you can test your problem2"

problems = []
problems.append(data)
problems.append(data2)



s = socket.socket()         # Create a socket object
host = "192.168.0.103" # Get local machine name
port = 4448       # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

 

pickle.dump( problems, open( "problem_data.b", "wb" ) )

f = open("problem_data.b","rb")
file_data = str(f.read())
f.close()
s.listen(5)                 # Now wait for client connection.
while True:
	c, addr = s.accept()     # Establish connection with client.
	connection_code= c.recv(1024)
	print "connection_code=",c
	if connection_code == 1000 :
		print "client normal connected"
	elif connection_code == 1001:
		print "client notification reciever connected"

	ready_to_send_status = str(3000)
	c.send(ready_to_send_status)

	connection_code=c.recv(100)
	if connection_code == 3001:
		print "hello"

   #print 'Got connection from', addr
	c.send(file_data)
	c.close()                # Close the connection








