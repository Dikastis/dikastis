import mysql.connector
from models import *
from datetime import *

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
	data_client = (_client_data.team_id, _client_data.team_name, _client_data.language, _client_data.filename, _client_data.problem_code,_client_data.submission_number)
    
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
	data_response = (_response_data.id, _response_data.language, _response_data.problem_code, _response_data.submission_number, _response_data.exec_time,_response_data.result)
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