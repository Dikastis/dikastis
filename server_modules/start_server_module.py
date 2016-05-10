import socket
import thread
import sys
from constants.network_constants import *
from server_modules.client_modules_for_server import start_judge
import tkMessageBox
from connection import *

def startServer(total_problems , q , s):
    sock = create_connection("",4475)
    thread.start_new_thread(start_handshaking,(sock,))


    # problem_choices = '' # all problems name and code will be here
    # for i in range(total_problems):
    #     problem_choices = problem_choices + q[i] + '&&&'
 
    # #Bind socket to local host and port
    # HOST = ''   # Symbolic name, meaning all available interfaces
    # PORT = 4444 
    # try:
    #     s.bind((HOST, PORT))
    # except socket.error as msg:
    #     print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    #     sys.exit()
     
    # print 'Socket bind complete'
 
    # #Start listening on socket
    # s.listen()
    # print 'Socket now listening'
 
    # #now keep talking with the client
    # while 1:
    #     #wait to accept a connection - blocking call
    #     conn, addr = s.accept()
    #     print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #     type = conn.recv(100)

    #     if type == "1000": # connection is client
    #         #starting judge
    #         thread.start_new_thread(start_judge,(conn,))
    #         pass
            
    #     elif type == "1001": # connection is client reciever
    #         pass
    #     elif type == "1002": #connection is server
    #         pass
    #     else:
    #         #handle error
    #         pass
    
    #     #sending all problems in this contest
    #     conn.send(problem_choices)
    
    #     #response recieved
    #     response = conn.recv(100)
    #     print response
    
    #     conn.send('ready to judge')

    #     #starting judge
    #     thread.start_new_thread(start_judge,(conn,))

     
    # s.close()
