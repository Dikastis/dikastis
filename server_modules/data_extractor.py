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
	else:
		return 0

