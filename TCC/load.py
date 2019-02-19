import api_util


def extract_owners(repositories_pages):
    for repositories in repositories_pages:
        for repository in repositories['items']:
            owner = api_util.get_user(repository['owner']['url'])
            print('Owner: ', owner['name'], owner['email'])
            print('Repository: ', repository['name'])
        # if(contributors != None):

def extract_contributors(repositories):
    for repository in repositories:
        contributors = api_util.get_contributors(repository)
        # if(contributors != None):


number_of_pages = 1
repositories_pages = []
for page in range(number_of_pages):
    # param format = term+language:python
    repositories_pages.append(api_util.search_repositories(query='language:python', page=page+1))
    extract_owners(repositories_pages)
    print(len(repositories_pages[page]['items']))
print(repositories_pages[0]['total_count'])
