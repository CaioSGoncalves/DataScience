import mysql.connector as connector 

class MySQL_Connector():
    _host_name = ''
    _port = 27017
    _cursor = None

    def __init__(self, host_name, user_name, password):
        self.create_connection(host_name, user_name,password)

    def create_connection(self, host_name, user_name, password):
        mydb = connector.connect(host_name, user_name, password)
        self._cursor = mydb.cursor()

    def create_database(self, db_name):
        print()

    def create_table(self, col_name, db_name):
        print()

    def insert_one(self, db_name, col_name, value):
        print()

    def insert_multiples(self, db_name, col_name, values):
        print()