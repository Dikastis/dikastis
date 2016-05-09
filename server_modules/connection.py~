import socket
import thread
from models import *
import pickle 
import heapq
from problem_data import *
from data_extractor import *

READY_TO_SEND = str(3000)
READY_TO_RECEIVE = str(3001)
DATA_RECEIVED_READY_FOR_NEXT = str(3002)
LOGIN_VERIFIED = str(200)
LOGIN_NOT_VERIFED = str(201)
SEND_QUEUE_SIZE = str(5000)


import heapq

server_load = []



#print heapq.heappop(server_load)

def create_connection(host='',port=4455):
	sock = socket.socket()         # Create a socket object
	#host = "" # Get local machine name
	#port = 4460   # Reserve a port for your service.
	sock.bind((host, port))        # Bind to the port
	print "socket binding complete"
	sock.listen(5)  
	return sock


def handshaking(sock):
	c, addr = sock.accept()     # Establish connection with client.
	connection_code = c.recv(100)

	if connection_code == "1000" :
		print "client normal connected"
		thread.start_new_thread(run_client,(c,))
		

	elif connection_code == "1001":
		print "client notification reciever connected"
		thread.start_new_thread(run_notification_client,(c,))
	
	elif connection_code == "2000":
		print "server connected"
		thread.start_new_thread(run_submission_server,(c,))

	


def run_client(conn):
	conn.send(READY_TO_RECEIVE)       #wainting for login credentials from client
	client_login_data = conn.recv(1024)
	(login_id,login_psw) = client_login_data.split(' ')
	print login_id
	print login_psw
	test_login = team_login()
	test_login.id = login_id
	test_login.password = login_psw

	
	result_of_login_authentication=authenticate(test_login)

	if result_of_login_authentication==1:
		print "client successfully verified"
		conn.send(LOGIN_VERIFIED)
		connection_code = conn.recv(100)

		if connection_code == READY_TO_RECEIVE:
			
			#problem_data = get_problem_data()
			#problem_data = problems_data(0)

			problem_data = get_problem_data("1")

			#TODO : add mechanism for huge data sending

			pickle.dump( problem_data, open( "problem_data.b", "wb" ) )
			f = open("problem_data.b","rb")
			file_data = str(f.read())
			f.close()
			conn.send(file_data)

			conn.send(DATA_RECEIVED_READY_FOR_NEXT)
			code_receive_from_client(conn)


			

	else:
		print "login not verified"
		conn.send(LOGIN_NOT_VERIFED) 
		run_client(conn)



def run_notification_client(conn):
	conn.send(READY_TO_SEND)
	connection_code = conn.recv(100)

	if connection_code == READY_TO_RECEIVE:
		dummy_notification = "broadcast$$$this is broadcast data"
		conn.send(dummy_notification)

		connection_code = conn.recv(100)
		if connection_code == DATA_RECEIVED_READY_FOR_NEXT:
			print "notification send successfull"



def run_submission_server(conn):
	conn.send(SEND_QUEUE_SIZE)

	queue_size = conn.recv(100)

	heapq.heappush(server_load,(int(queue_size),conn))

	conn.send(READY_TO_SEND)




def code_receive_from_client(conn):

	received_data = conn.recv(1024)
	conn.send(DATA_RECEIVED_READY_FOR_NEXT)

	#data = received_data.split(" ")
	print "data going to receive"
	submission_details = problem_submission_from_client(0);
	#submission_details.problem_code = data[0]
	#submission_details.language = data[1]
	#submission_details.submission_number = data[1]
	submission_details.problem_code = received_data

	print submission_details.problem_code

	total = ""
	data = conn.recv(1000)
	while data != "":
		total = total  + data
		print total
		data = conn.recv(1000)

	submission_details.problem_statement = data
	print submission_details.problem_statement

	#thread.start_new_thread(send_to_judge,(conn,submission_details,))

	conn.send(DATA_RECEIVED_READY_FOR_NEXT)

	code_receive_from_client(conn)


def send_to_judge(conn,submission_details):

	q_size,conn_sub_server = heapq.heappop(server_load)

	conn_sub_server.send("testing hello")





def start_handshaking(sock):
    while True:
    	handshaking(sock)





#sock = create_connection()
#while True:
#	handshaking(sock)









