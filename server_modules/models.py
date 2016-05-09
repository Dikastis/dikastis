class client_data(object):
	def __init__(self,object):
		self.team_id = ""
		self.team_name = ""
		self.problem_code = ""
		self.language = ""
		self.time_stamp = ""
		self.file_name = ""
		self.submission_number = 0

class calc_server_data(object):
	def __init__(self,object):
		self.ip = "" 
		self.port = ""
		self.queue_size = ""


class problems_data(object):
	def __init__(self,object):
		self.problem_id = ""
		self.problem_code = ""
		self.problem_name = ""
		self.problem_statement = ""


class team_login:
	def __init__(self):
		self.id = ""
		self.password  = ""

class response_data(object):
	def __init__(self,object):
		self.id = ""
		self.language = ""
		self.time_stamp = ""
		self.problem_code = ""
		self.submission_number = ""
		self.exec_time = ""
		self.result = ""
		self.memory = ""

class client_connections_data(object):
	def __init__(self,object):
		self.ip = ""
		self.port = ""
		self.serial_key = ""
		self.sender_port = ""
		self.receiver_port = ""


class problem_submission_from_client(object):
	def __init__(self,object):
		self.problem_code= ""
		self.problem_language=""
		self.problem_statement=""
		self.conn = ""

	def display():
		print self.problem_code
		print self.problem_language
		print self.problem_statement
		print self.conn

