import requests

class APIHelper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        # self.session.headers.update(self.headers)
        
    def call_get_api(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        return response.json()
    
    def call_post_api(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url , json=data)
        response.raise_for_status()
        return response.json()