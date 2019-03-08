from Loaders.mongo_loader import Mongo_Loader

loader = Mongo_Loader(host_name='localhost')

# query parameter format = term + '+language:'+ language
# loader.collect_data(query='language:python', number_of_pages=1)
# loader.insert_data(db_name='github_twitter')