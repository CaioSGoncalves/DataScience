import os
from api_base import API_Base
from credentials import GIT_USER, GIT_TOKEN

class API_GitHub(API_Base):

    def __init__(self, user=None, token=None):
        self.user = user or GIT_USER
        self.token = token or GIT_TOKEN
        self.headers = {'User-Agent': self.user, "Authorization": "token {token}".format(token=self.token)}
        super().__init__('https://api.github.com')


    def search_repositories(self, query=None, page=None, per_page=10):
        params = {'q':query,'per_page':per_page,'sort':'stars','order':'desc','page':page}
        return super().make_request(self._url_base+'/search/repositories', params)

    def get_user(self, url):
        return super().make_request(url)

    def get_contributors(self, repository):
        url = repository['url'] + '/contributors'
        contributors = super().make_request(url)
        return [self.get_user(contributor['url']) for contributor in contributors]