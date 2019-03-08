from urllib.parse import urlparse
from APIs.api_github import API_GitHub
from APIs.api_twitter import API_Twitter

_api_github = API_GitHub()
_api_twitter = API_Twitter()

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
                if(twitter_user is not None):
                    twitter_user['tweets'] = _api_twitter.get_user_tweets(twitter_screen_name)
                    twitter_data[github_login] = twitter_user
        return twitter_data

def collect_repositories(query, number_of_pages):
    print('Collecting repositories: ' + str(query))
    repositories = list()
    for page in range(number_of_pages):
        print('Page', page)
        repository = _api_github.search_repositories(query=query, page=page+1)
        if (repository is not None):
            repositories.extend(repository['items'])
    return repositories