import socket
import thread
from models import *
import pickle 
import problem_data

READY_TO_SEND = str(3000)
READY_TO_RECEIVE = str(3001)
DATA_RECEIVED_READY_FOR_NEXT = str(3002)
LOGIN_VERIFIED = str(200)
LOGIN_NOT_VERIFED = str(201)

def create_connection(host='',port=4444):
	sock = socket.socket()         # Create a socket object
	host = "" # Get local machine name
	port = 4448       # Reserve a port for your service.
	sock.bind((host, port))        # Bind to the port
	print "socket binding complete"
	sock.listen(5)  
	return sock


def handshaking(sock):
	c, addr = sock.accept()     # Establish connection with client.
	connection_code = c.recv(100)

	if connection_code == 1000 :
		print "client normal connected"
		run_client(c)

	elif connection_code == 1001:
		print "client notification reciever connected"
		run_notification_client(c)

	elif connection_code == 2000:
		print "server connected"
		run_submission_server(c)

	c.close() 


def run_client(conn):
	conn.send(READY_TO_RECEIVE)       #wainting for login credentials from client
	client_login_data = conn.recv(1024)
	(login_id,login_psw) = client_login_data.split(' ')
	test_login = team_login()
	test_login.id = login_id
	test_login.password = login_psw
	
	result_of_login_authentication=authenticate(test_login)

	if result_of_login_authentication==1:
		print "client successfully verified"
		conn.send(LOGIN_VERIFIED)
		connection_code = conn.recv(100)

		if connection_code == 200:
			problem_data = get_problem_data()
			
			pickle.dump( problems, open( "problem_data.b", "wb" ) )

			f = open("problem_data.b","rb")
			file_data = str(f.read())
			f.close()
			c.send(file_data)

	else:
		print "login not verified"
		conn.send(LOGIN_NOT_VERIFED) 
		run_client(conn)



def run_notification_client(conn):
	conn.send(READY_TO_SEND)
	connection_code = conn.recv(100)

	if connection_code == READY_TO_RECEIVE:
		dummy_notification = "B this is broadcast data"
		conn.send(dummy_notification)

		connection_code = conn.recv(100)
		if connection_code == DATA_RECEIVED_READY_FOR_NEXT:
			print "notification send successfull"


sock = create_connection()
handshaking(sock)








