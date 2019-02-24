from api_github import API_GitHub
from mongo_connect import MongoDB_Util
from urllib.parse import urlparse

_api_github = API_GitHub()
database_util = MongoDB_Util('localhost')


def collect_contributors(repositories):
    print('Collecting contributors: ')
    contributors_twitter = dict()
    for repository in repositories:
        contributors = _api_github.get_contributors(repository)
        for contributor in contributors:
            if contributor is not None:
                have_twitter = 'twitter' in urlparse(contributor['blog']).netloc
                already_inserted = contributor['login'] in contributors_twitter
                if (have_twitter and not already_inserted):
                    contributor['repositories'] = [repository]
                    contributors_twitter[contributor['login']] = contributor
                    print('OK + ' + contributor['blog'] + ' repository ' + repository['name'])
                elif (have_twitter and already_inserted):
                        contributor_inserted = contributors_twitter[contributor['login']]
                        contributor_inserted['repositories'].append(repository)
                        print('passou aqui ' + contributor_inserted['blog'] + ' repository ') 
                        print(contributor_inserted['repositories'])
    return list(contributors_twitter.values())


# def collect_owners(repositories):
#     print('Collecting owners')
#     owners = list()
#     for repository in repositories:
#         owner = _api_github.get_user(repository['owner']['url'])
#         owners.append(owner)
#     return owners


def collect_repositories(query, number_of_pages):
    print('Collecting repositories: ' + str(query))
    repositories = list()
    for page in range(number_of_pages):
        print('Page', page)
        # query parameter format = term+language:python
        repository = _api_github.search_repositories(query=query, page=page+1)
        if (repository is not None):
            repositories.extend(repository['items'])
    return repositories


def collect_data(query, number_of_pages):
    values_dict = dict()
    # values_dict['repositories']
    repositories = collect_repositories(query, number_of_pages)
    # values_dict['owners'] = collect_owners(values_dict['repositories'])
    values_dict['users'] = collect_contributors(repositories)
    return values_dict


def insert_data(db_name, values_dict):
    for col_name, values in values_dict.items():
        print('Inserting ' + col_name)
        database_util.insert_multiples(db_name, col_name, values)


values_dict = collect_data(query='language:python', number_of_pages=5)

# insert_data(db_name='git_hub', values_dict=values_dict)
# organize_data
