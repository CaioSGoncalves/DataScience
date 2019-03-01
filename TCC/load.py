import load_util as util


values_dict = util.collect_data(query='language:python', number_of_pages=1)
util.insert_data(db_name='github_twitter', values_dict=values_dict)
