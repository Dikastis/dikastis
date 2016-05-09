import mysql.connector
from models import *
from datetime import *
import copy

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'dikastis_db',
  'raise_on_warnings': True,
}



def add_client_details( _client_data):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_client = ("INSERT INTO client_details "
               "(team_id, team_name, language, file_name,problem_code,submission_number) "
 				"VALUES (%s, %s, %s, %s, %s,%s)")
	data_client = (_client_data.team_id, _client_data.team_name, _client_data.language, _client_data.file_name, _client_data.problem_code,_client_data.submission_number)
    
	cursor.execute(add_client, data_client)
	cnx.commit()
	cursor.close()
	cnx.close()

def add_servers(_calc_server_data):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_server = ("INSERT INTO servers"
				"(server_ip, server_port, queue_size )"
				"VALUES (%s, %s, %s) ")
	data_server = (_calc_server_data.ip, _calc_server_data.port, _calc_server_data.queue_size)

	cursor.execute(add_server,data_server)
	cnx.commit()
	cursor.close()
	cnx.close()

def authenticate(_team_login):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	authenticate = ("SELECT team_id "
				"FROM team_credentials "
				"WHERE team_id = %s AND team_pass = %s")
	data_login = (_team_login.id,_team_login.password)

	cursor.execute(authenticate,data_login)
	(number_of_rows,)=cursor.fetchone()
	
	cnx.commit()
	cnx.close()

	if number_of_rows > 0:
		return 1

def add_response_data(_response_data):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	response = ("INSERT INTO response"
				"(team_id, language, problem_code, submission_number, execution_time, judgment, memory )"
				"VALUES (%s, %s, %s, %s, %s, %s, %s) ")
	data_response = (_response_data.id, _response_data.language, _response_data.problem_code, _response_data.submission_number, _response_data.exec_time,_response_data.result, _response_data.memory)
	cursor.execute(response,data_response)
	cnx.commit()
	cnx.close()

def add_problem_data(_problems_data):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	problem = ("INSERT INTO problems"
				"( problem_name, problem_code, problem_statement )"
				"VALUES (%s, %s, %s) ")
	data_problem = (_problems_data.problem_name, _problems_data.problem_code, _problems_data.problem_statement)
	cursor.execute(problem,data_problem)
	cnx.commit()
	cnx.close()

def add_client_connections(_client_connections):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	connection = ("INSERT INTO client_connections"
				"(ip, port, serial_key, sender_port, receiver_port)"
				"VALUES (%s,%s,%s,%s,%s)")
	data_connection = (_client_connections.ip,_client_connections.port,_client_connections.serial_key,_client_connections.sender_port, _client_connections.receiver_port)

	cursor.execute(connection,data_connection)
	cnx.commit()
	cnx.close()

# def get_client_data(request):
# 	print request



def get_auth(request):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	authenticate = ("SELECT team_id "
				"FROM team_credentials "
				"WHERE "+request)
	print request
	data_login = ()

	cursor.execute(authenticate,data_login)
	(number_of_rows,)=cursor.fetchone()
	
	cnx.commit()
	cnx.close()

	if number_of_rows > 0:
		return 1


def get_client_data(request):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_client = ("SELECT *"
				"FROM client_details "
				"WHERE "+request)
	cursor.execute(add_client)
	row = cursor.fetchall()
	# data = [client_data for _ in range(10)]
	data = []
	i = 0
	for i in range(len(row)):
		new_data = client_data(i)
		new_data.team_id = format(row[i][0])
		new_data.team_name = format(row[i][1])
		new_data.problem_code = format(row[i][2])
		new_data.language = format(row[i][3])
		new_data.time_stamp = format(row[i][4])
		new_data.file_name = format(row[i][5])
		new_data.submission_number = format(row[i][6])
		data.append(new_data)

	cnx.commit()
	cursor.close()
	cnx.close()
	return data

def get_server_data(request):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_client = ("SELECT *"
				"FROM servers "
				"WHERE "+request)
	cursor.execute(add_client)
	row = cursor.fetchall()
	# data = [client_data for _ in range(10)]
	data = []
	i = 0
	for i in range(len(row)):
		new_data = calc_server_data(i)
		new_data.ip = format(row[i][0])
		new_data.port = format(row[i][1])
		new_data.queue_size = format(row[i][2])
		data.append(new_data)

	cnx.commit()
	cursor.close()
	cnx.close()
	return data

def get_problem_data(request):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_client = ("SELECT *"
				"FROM problems "
				"WHERE "+request)
	cursor.execute(add_client)
	row = cursor.fetchall()
	# data = [client_data for _ in range(10)]
	data = []
	i = 0
	for i in range(len(row)):
		new_data = problems_data(i)
		new_data.problem_id = format(row[i][0])
		new_data.problem_name = format(row[i][1])
		new_data.problem_code = format(row[i][2])
		new_data.problem_statement = format(row[i][3])
		data.append(new_data)

	cnx.commit()
	cursor.close()
	cnx.close()
	return data

def get_response_data(request):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_client = ("SELECT *"
				"FROM response "
				"WHERE "+request)
	cursor.execute(add_client)
	row = cursor.fetchall()
	# data = [client_data for _ in range(10)]
	data = []
	i = 0
	for i in range(len(row)):
		new_data = response_data(i)
		new_data.id = format(row[i][0])
		new_data.language = format(row[i][1])
		new_data.time_stamp = format(row[i][2])
		new_data.problem_code = format(row[i][3])
		new_data.submission_number = format(row[i][4])
		new_data.exec_time = format(row[i][5])
		new_data.result = format(row[i][6])
		new_data.memory = format(row[i][7])
		data.append(new_data)

	cnx.commit()
	cursor.close()
	cnx.close()
	return data


def get_connections_data(request):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_client = ("SELECT *"
				"FROM client_connections "
				"WHERE "+request)
	cursor.execute(add_client)
	row = cursor.fetchall()
	# data = [client_data for _ in range(10)]
	data = []
	i = 0
	for i in range(len(row)):
		new_data = client_connections_data(i)
		new_data.ip = format(row[i][0])
		new_data.port = format(row[i][1])
		new_data.serial_key = format(row[i][2])
		new_data.sender_port = format(row[i][3])
		new_data.receiver_port = format(row[i][4])
		data.append(new_data)

	cnx.commit()
	cursor.close()
	cnx.close()
	return data