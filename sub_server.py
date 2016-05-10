import socket
import thread
from server_modules.models import *
import pickle 
import heapq
from server_modules.problem_data import *
from server_modules.data_extractor import *
from server_modules.queue_file import *

READY_TO_SEND = str(3000)
READY_TO_RECEIVE = str(3001)
DATA_RECEIVED_READY_FOR_NEXT = str(3002)
LOGIN_VERIFIED = str(200)
LOGIN_NOT_VERIFED = str(201)
SEND_QUEUE_SIZE = str(5000)

I_M_SERVER = str(2000)

submission_queue = Queue()




s = socket.socket()         # Create a socket object
host = ''      # Get local machine name
port = 4475   # Reserve a port for your service.

s.connect((host, port))

s.send(I_M_SERVER)

connection_code = s.recv(100)
print connection_code

if connection_code == "5000":
    s.send(str(submission_queue.size()))

    print submission_queue.size()

    number_of_problems = int(s.recv(100))

    s.send(DATA_RECEIVED_READY_FOR_NEXT)
    print number_of_problems

    for i in range(0,number_of_problems):
        problem_code = s.recv(100)
        s.send(DATA_RECEIVED_READY_FOR_NEXT)
        print problem_code

        input_file_name = problem_code + ".in"
        file = open(input_file_name,"w")
        input_data = s.recv(10000)
        file.write(input_data)
        print input_data

        s.send(DATA_RECEIVED_READY_FOR_NEXT)

        output_file = problem_code + ".out"
        file = open(output_file,"w")
        output_data = s.recv(10000)
        file.write(output_data)
        print output_data
        s.send(DATA_RECEIVED_READY_FOR_NEXT)

        print "obj num ",i
    #########################################
    data = s.recv(100000)

    f = open('submission_sub.b','wb')
    f.write(data)
    f.close()
    print "data data_received"
    data_recieved=pickle.load(open('submission_sub.b','rb'))

    data_recieved.display()

    file_name = data_recieved.conn + data_recieved.problem_code + ".cpp"

    f = open(file_name,'w')
    f.write(data_recieved.problem_statement)
    f.close()

    a=soldier.run("python checker.py "+"test "+name)


















