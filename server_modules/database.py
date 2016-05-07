import mysql.connector
from mysql.connector import errorcode
from tables import TABLES

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)



config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'dikastis_db',
  'raise_on_warnings': True,
}


try:
	cnx = mysql.connector.connect(**config)

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)

DB_NAME = config['database']

try:
    cnx.database = DB_NAME    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

cursor = cnx.cursor()




for name, ddl in TABLES.iteritems():
    try:
    	end=''
        print("Creating table {}: ".format(name), end)
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()