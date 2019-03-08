from DataModelers import mongo_modeler
from Connectors import mongo_connector
from Loaders.base_loader import Loader

class Mongo_Loader(Loader):
        def __init__(self, host_name):
                self.modeler = mongo_modeler
                self.connector = mongo_connector.MongoDB_Connector(host_name)

        def insert_data(self, db_name):
                for col_name, values in self.modeled_data.items():
                        print('Inserting ' + col_name)
                        self.connector.bulk_upsert_many(db_name, col_name, values)