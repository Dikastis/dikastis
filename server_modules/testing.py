from models import *
from data_extractor import *

data = client_data()
data.team_id = "test126"
data.team_name = "test test"
data.problem_code = "q1"
data.language = "C++"
#data.timestamp = 1462698376
file = open("data.txt","r")
data.filename = file.read()
data.submission_number = 1

add_client_details(data)
