from models import *
from data_extractor import *

def get_problem_data():
	data = problems_data()
	data.problem_code = "q1"
	data.problem_name = "testing problem"
	data.problem_statement = "this is a testing problem.Here you can test your problem"

	data2 = problems_data()
	data2.problem_code = "q2"
	data2.problem_name = "testing problem2"
	data2.problem_statement = "this is a testing problem.Here you can test your problem2"

	problems = []
	problems.append(data)
	problems.append(data2)

	return problems
