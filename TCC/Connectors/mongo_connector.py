import pymongo
from pymongo.operations import ReplaceOne

class MongoDB_Connector():
    _host_name = ''
    _port = 27017
    _client = None

    def __init__(self, host_name):
        self._host_name = host_name
        self._client = pymongo.MongoClient(self._host_name, self._port)
    
    def create_database(self, db_name):
        database = self._client[db_name]
        return database

    def create_collection(self, col_name, db_name):
        db = self._client[db_name]
        collection = db[col_name]
        return collection

    def insert_one(self, db_name, col_name, value):
        db = self._client[db_name]
        col = db[col_name]
        id_inserted = col.insert_one(value) 
        return id_inserted

    def insert_multiples(self, db_name, col_name, values):
        db = self._client[db_name]
        col = db[col_name]
        id_inserted = col.insert_many(values) 
        return id_inserted

    def drop_collection(self, col_name, db_name):
        db = self._client[db_name]
        collection = db[col_name]
        return collection.drop()

    def upsert_many(self, db_name, col_name, values):
        db = self._client[db_name]
        col = db[col_name]
        for value in values:
            col.update({'_id':value['_id']}, value, upsert=True)

    def bulk_upsert_many(self, db_name, col_name, values):
        db = self._client[db_name]
        col = db[col_name]
        operations = [ ReplaceOne(filter={'_id':value['_id']}, replacement=value, upsert=True) for value in values ]
        result = col.bulk_write(operations, ordered=False)
