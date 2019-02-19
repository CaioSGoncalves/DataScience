import json
import requests
from urllib.parse import urlencode

url_base_github = 'https://api.github.com'

def make_request(url, params=None):
    response = requests.get(url, params)    
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
    return None

def search_repositories(query=None, page=None, per_page=10):
    params = {'q':query,'per_page':per_page,'sort':'stars','order':'desc'}
    return make_request(url_base_github+'/search/repositories', params)



def get_user(url):
    return make_request(url)

def get_contributors(repository):
    params = {''}
    return 3    



