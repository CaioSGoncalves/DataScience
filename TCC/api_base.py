import json
import requests

class API_Base:

    _url_base = ''

    def __init__(self, url):
        self._url_base = url

    def make_request(self, url, params=None):
        response = requests.get(url, params)    
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        return None