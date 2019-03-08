import json
import requests
from time import sleep

class API_Base:

    _url_base = ''
    headers = dict()
    auth = None

    def __init__(self, url, auth=None):
        self._url_base = url
        self.auth = auth

    def make_request(self, url, params=None):
        response = requests.get(url, params, headers=self.headers, auth=self.auth)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        print(response.status_code)
        return None