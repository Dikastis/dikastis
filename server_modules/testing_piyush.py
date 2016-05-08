from models import *
from data_extractor import *

data = client_connections_data()
data.ip = "127.0.0.1"
data.port = "1035"
data.serial_key = "1251jkcknd"
data.sender_port = "1542"
data.receiver_port = "8562"

add_client_connections(data)
