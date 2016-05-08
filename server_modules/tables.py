TABLES = {}

TABLES['client_details'] = (
    "CREATE TABLE client_details ("
    "  team_id varchar(100) NOT NULL,"
    "  team_name varchar(100) NOT NULL,"
    "  language varchar(50) NOT NULL,"
    "  file_name LONGBLOB NOT NULL,"
    "  time_stamp timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,"
    "  problem_code varchar(100) NOT NULL,"
    "  submission_number integer NOT NULL,"
    "  PRIMARY KEY (team_id,problem_code,submission_number)"
    ") ENGINE=InnoDB")

TABLES ['response'] = (
    "CREATE TABLE response ("
    "  team_id varchar(100) NOT NULL,"
    "  language varchar(50) NOT NULL,"
    "  time_stamp timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,"
    "  problem_code varchar(100) NOT NULL,"
    "  submission_number integer NOT NULL,"
    "  execution_time integer NOT NULL,"
    "  judgment integer NOT NULL,"
    "  memory integer,"
    "  PRIMARY KEY (team_id,problem_code,submission_number)"
    ") ENGINE=InnoDB")


TABLES ['servers'] = (
    "CREATE TABLE servers ("
    "  server_ip varchar(100) NOT NULL,"
    "  server_port varchar(50) NOT NULL,"
    "  queue_size varchar(50) NOT NULL,"
    "  PRIMARY KEY (server_ip)"
    ") ENGINE=InnoDB")

TABLES ['problems'] =(
    "CREATE TABLE problems ("
    "   problem_id bigint auto_increment NOT NULL,"
    "   problem_name varchar(50) NOT NULL,"
    "   problem_code varchar(50) NOT NULL,"
    "   problem_statement text NOT NULL,"
    "   PRIMARY KEY(problem_name,problem_code,problem_statement)"
    ") ENGINE=InnoDB")

TABLES ['team_credentials'] = (
    " CREATE TABLE team_credentials("
    "   team_id varchar(100) NOT NULL,"
    "   team_pass varchar(100) NOT NULL"
    ") ENGINE=InnoDB")

TABLES ['client_connections'] = (
    " CREATE TABLE client_connections("
    "   ip varchar(100) NOT NULL PRIMARY KEY ,"
    "   port varchar(20) NOT NULL,"
    "   serial_key varchar(100) NOT NULL,"
    "   sender_port varchar(20) NOT NULL,"
    "   receiver_port varchar(20) NOT NULL"
    ") ENGINE=InnoDB")