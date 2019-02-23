from api_base import API_Base

class API_GitHub(API_Base):

    def __init__(self):
        super().__init__('https://api.github.com')

    def search_repositories(self, query=None, page=None, per_page=10):
        params = {'q':query,'per_page':per_page,'sort':'stars','order':'desc'}
        return super().make_request(self._url_base+'/search/repositories', params)

    def get_user(self, url):
        return super().make_request(url)

    def get_contributors(self, repository):
        params = {''}
        return 3    



