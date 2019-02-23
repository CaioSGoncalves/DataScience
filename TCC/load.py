from api_github import API_GitHub
from mongo_connect import MongoDB_Util

_api_github = API_GitHub()
database_util = MongoDB_Util('localhost')


def collect_contributors(repositories):
    print('Collecting contributors: ')
    for repository in repositories:
        contributors = _api_github.get_contributors(repository)

def collect_owners(repositories):
    print('Collecting owners')
    owners = list()
    for repository in repositories:
        owners.append(_api_github.get_user(repository['owner']['url']))
        # print('Owner: ', owner['name'], owner['email'])
        # print('Repository: ', repository['name'])
    return owners

def collect_repositories(query, number_of_pages):
    print('Collecting repositories: ' + str(query))
    repositories = list()
    for page in range(number_of_pages):
        # query parameter format = term+language:python
        repositories.extend(_api_github.search_repositories(query=query, page=page+1)['items'])
    #print(repositories[0]['total_count'])
    return repositories

def collect_data(query, number_of_pages):
    values_dict = dict()
    values_dict['repositories'] = collect_repositories(query, number_of_pages)
    values_dict['owners'] = collect_owners(values_dict['repositories'])
    # contributors = collect_contributors(repositories)
    return values_dict

def insert_data(db_name, values_dict):
    for col_name, values in values_dict.items():
        print('Inserting ' + col_name)
        database_util.insert_multiples(db_name, col_name, values)


values_dict = collect_data(query='language:python', number_of_pages=1)

insert_data(db_name='git_hub', values_dict=values_dict)
