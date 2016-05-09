from models import *
from data_extractor import *


# data = client_connections_data(0)
data = get_connections_data("1")
print len(data)
print data[0].sender_port