class client_data:
	def __init__(self):
		self.team_id = ""
		self.team_name = ""
		self.problem_code = ""
		self.language = ""
		self.time_stamp = ""
		self.file_name = ""
		self.submission_number = 0
		

	def display_data():
		print self.team_id
		print self.team_name
		print self.problem_code
		print self.language
		print self.timestamp


class calc_server_data:
	def __init__(self):
		self.ip = "" 
		self.port = ""
		self.queue_size = ""

class problems_data:
	def __init__(self):
		self.problem_code = ""
		self.problem_data = ""
		self.problem_statement = ""

	def display_problem_data():
		print self.problem_code
		print self.problem_name
		print self.problem_statement

class team_login:
	def __init__(self):
		self.id = ""
		self.password  = ""


class problem_submission_from_client(object):
	def __init__(self,object=0):
		self.problem_code= ""
		self.problem_language=""
		self.problem_statement=""
		self.conn = ""

	def display(self):
		print self.problem_code
		print self.problem_language
		print self.problem_statement
		print self.conn

