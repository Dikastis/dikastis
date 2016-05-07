TABLES = {}

TABLES['client_details'] = (
    "CREATE TABLE client_details ("
    "  team_code varchar(100) NOT NULL,"
    "  ip varchar(100) NOT NULL,"
    "  port integer NOT NULL,"
    "  language varchar(50) NOT NULL,"
    "  file_name LONGBLOB NOT NULL,"
    "  time_stamp timestamp NOT NULL,"
    "  problem_code varchar(100) NOT NULL,"
    "  submission_number integer NOT NULL,"
    "  PRIMARY KEY (team_code,problem_code,submission_number)"
    ") ENGINE=InnoDB")

TABLES ['response'] = (
    "CREATE TABLE response ("
    "  team_code varchar(100) NOT NULL,"
    "  language varchar(50) NOT NULL,"
    "  time_stamp timestamp NOT NULL,"
    "  problem_code varchar(100) NOT NULL,"
    "  submission_number integer NOT NULL,"
    "  execution_time integer NOT NULL,"
    "  judgment integer NOT NULL,"
    "  memory integer,"
    "  PRIMARY KEY (team_code,problem_code,submission_number)"
    ") ENGINE=InnoDB")