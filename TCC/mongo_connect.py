import pymongo

class MongoDB_Util():
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


# teste = MongoDB_Util('localhost')
# values = [
#             { "name": "Amy", "address": "Apple st 652"},
#             { "name": "Hannah", "address": "Mountain 21"},
#             { "name": "Michael", "address": "Valley 345"},
#             { "name": "Sandy", "address": "Ocean blvd 2"},
#             { "name": "Betty", "address": "Green Grass 1"},
#             { "name": "Richard", "address": "Sky st 331"},
#             { "name": "Susan", "address": "One way 98"},
#             { "name": "Vicky", "address": "Yellow Garden 2"},
#             { "name": "Ben", "address": "Park Lane 38"},
#             { "name": "William", "address": "Central st 954"},
#             { "name": "Chuck", "address": "Main Road 989"},
#             { "name": "Viola", "address": "Sideway 1633"}
#         ]

# teste.insert_multiples('db1',  'col1', values)
