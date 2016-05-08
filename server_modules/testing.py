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

data = problem_data()
data.problem_code = "q1"
data.problem_name = "testing problem"
data.problem_statement = "this is a testing problem.Here you can test your problem"

HOST = ""
PORT = 4884

              # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12348               # Reserve a port for your service.

s.connect((host, port))



problem_data = pickle.load(data)

print s.recv(1024)
s.close                     # Close the socket when done



