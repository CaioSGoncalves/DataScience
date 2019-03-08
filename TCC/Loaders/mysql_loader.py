from DataModelers import mysql_modeler
from Connectors import mysql_connector
from Loaders.base_loader import Loader

class MySQl_Loader(Loader):
        def __init__(self, host_name, user_name, password):
                self.modeler = mysql_modeler
                self.connector = mysql_connector.MySQL_Connector(host_name, user_name, password)

        def insert_data(self, db_name):
                for col_name, values in self.modeled_data.items():
                        print('Inserting ' + col_name)
                        self.connector.bulk_upsert_many(db_name, col_name, values)