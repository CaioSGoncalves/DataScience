from api_github import API_GitHub
from api_twitter import API_Twitter
from mongo_connect import MongoDB_Util
from urllib.parse import urlparse

_api_github = API_GitHub()
_api_twitter = API_Twitter()
database_util = MongoDB_Util('localhost')


def collect_contributors(repositories):
    print('Collecting contributors')
    contributors = dict()
    contributors_twitter = dict()
    for repository in repositories:
        repo_contributors = _api_github.get_contributors(repository)
        for contributor in repo_contributors:
            if contributor is not None:
                contributor['have_twitter'] = 'twitter' in urlparse(contributor['blog']).netloc
                already_inserted = contributor['login'] in contributors
                if (not already_inserted):
                    contributor['contributor_repositories'] = [repository]
                    contributors[contributor['login']] = contributor
                    if (contributor['have_twitter']):
                        contributors_twitter[contributor['login']] = contributor['blog']
                else:
                    contributor_inserted = contributors[contributor['login']]
                    contributor_inserted['contributor_repositories'].append(repository)
    return contributors, contributors_twitter

def collect_twitter_data(github_with_twitter):
        print('Collecting twitter_data')
        twitter_data = dict()
        for github_login, twitter_link in github_with_twitter.items():
                twitter_screen_name = twitter_link.split('/')[-1]
                twitter_user = _api_twitter.get_user(twitter_screen_name)
                twitter_user['tweets'] = _api_twitter.get_user_tweets(twitter_screen_name)
                twitter_data[github_login] = twitter_user
        return twitter_data

def link_data(github_profiles, twitter_profiles, query):
        print('Linking data')
        user_data = list()
        for github_login, _ in github_profiles.items():
                user = dict()
                user['_id'] = github_profiles[github_login]['id']
                user['github_login'] = github_login
                user['have_twitter'] = github_profiles[github_login]['have_twitter']
                user['github'] = github_profiles[github_login]
                user['twitter'] = twitter_profiles.get(github_login)
                user['tag'] = query
                user_data.append(user) 
        return user_data

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
    print('Number of Repositories Collected: ', len(repositories))
    # values_dict['owners'] = collect_owners(values_dict['repositories'])
    # values_dict['users'] = collect_contributors(repositories)
    github_profiles, github_with_twitter = collect_contributors(repositories)
    print('Number of GitHub Users Collected: ', len(github_profiles))
    print('Number of GitHub Users with Twitter Collected: ', len(github_with_twitter))
    twitter_profiles = collect_twitter_data(github_with_twitter)
    values_dict['users'] = link_data(github_profiles, twitter_profiles, query)
    return values_dict


def insert_data(db_name, values_dict):
    for col_name, values in values_dict.items():
        print('Inserting ' + col_name)
        database_util.insert_multiples(db_name, col_name, values)