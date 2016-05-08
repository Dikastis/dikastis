class client_data:
	def __init__(self):
		self.team_id = ""
		self.team_name = ""
		self.problem_code = ""
		self.language = ""
		self.time_stamp = ""
		self.file_name = ""
		self.submission_number = 0


class calc_server_data:
	def __init__(self):
		self.ip = "" 
		self.port = ""
		self.queue_size = ""


class problems_data:
	def __init__(self):
		self.problem_id = ""
		self.problem_code = ""
		self.problem_name = ""
		self.problem_statement = ""


class team_login:
	def __init__(self):
		self.id = ""
		self.password  = ""

class response_data:
	def __init__(self):
		self.id = ""
		self.language = ""
		self.time_stamp = ""
		self.problem_code = ""
		self.submission_number = ""
		self.exec_time = ""
		self.result = ""
		self.memory = ""

class client_connections_data():
	def __init__(self):
		self.ip = ""
		self.port = ""
		self.serial_key = ""
		self.sender_port = ""
		self.receiver_port = ""
