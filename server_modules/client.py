#!/usr/bin/python           # This is client.py file
import pickle
import socket               # Import socket module
from models import *
from data_extractor import *

s = socket.socket()         # Create a socket object
host = "192.168.0.103" # Get local machine name
port = 4444              # Reserve a port for your service.

s.connect((host, port))



favorite_color = pickle.load( open( "problem_data.b", "rb" ) )
# favorite_color is now { "lion": "yellow", "kitty": "red" }


print s.recv(1024)
s.close                     # Close the socket when done
