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
               "(team_code, team_name, language, file_name,problem_code,submission_number) "
 				"VALUES (%s, %s, %s, %s, %s,%s)")
	data_client = (_client_data.team_id, _client_data.team_name, _client_data.language, _client_data.filename, _client_data.problem_code,_client_data.submission_number)
    
	cursor.execute(add_client, data_client)
	cnx.commit()
	cursor.close()
	cnx.close()