from models import *
from data_extractor import *

data = team_login
data.id = "1000"
data.password = "chutia"
# data.team_id = "test126"
# data.team_name = "test test"
# data.problem_code = "q1"
# data.language = "C++"
# #data.timestamp = 1462698376
# file = open("data.txt","r")
# data.filename = file.read()
# data.submission_number = 2

# add_client_details(data)

#add_servers(data)
print authenticate(data)