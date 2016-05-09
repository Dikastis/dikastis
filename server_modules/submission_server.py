import socket
import thread
from models import *
import pickle 
import heapq
from problem_data import *
from data_extractor import *
from queue_file import *

READY_TO_SEND = str(3000)
READY_TO_RECEIVE = str(3001)
DATA_RECEIVED_READY_FOR_NEXT = str(3002)
LOGIN_VERIFIED = str(200)
LOGIN_NOT_VERIFED = str(201)
SEND_QUEUE_SIZE = str(5000)

I_M_SERVER = str(2000)

submission_queue = Queue()




s = socket.socket()         # Create a socket object
host = "172.16.86.159"      # Get local machine name
port = 4466    # Reserve a port for your service.

s.connect((host, port))

s.send(I_M_SERVER)

connection_code = s.recv(100)
print connection_code

if connection_code == "5000":
	s.send(str(submission_queue.size()))

	connection_code = s.recv(100)
	print connection_code

	data = s.recv(100000)

	f = open('submission_sub.b','wb')
	f.write(data)
	f.close()
	
	data_recieved=pickle.load(open('submission_sub.b','rb'))

	print data_recieved.display










