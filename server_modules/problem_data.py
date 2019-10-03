from models import *
from data_extractor import *

def get_problem_data():
	data = problems_data(0)
	data.problem_code = "q1"
	data.problem_name = "testing problem"
	data.problem_statement = "this is a testing problem.Here you can test your problem"

	

	return data
